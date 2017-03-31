import random

from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.utils import timezone
from django.urls import reverse

from datetime import datetime

# Create your views here.
from .models import Beverage
from .models import Order

from main.models import Image
from main.models import User
# from .models import SeogyodongOrder
from .forms import OrderForm
from .forms import IdentifyForm
# from .forms import SeogyoOrderForm

from twilio.rest import TwilioRestClient


def _get_pin(length=5):
    return random.sample((range(10**(length-1), 10**length), 1)[0], 1)


def _verify_pin(phone_num, pin):
    return pin == cache.get(phone_num)[0]


def ajax_send_pin(request):
    """ Sends SMS PIN to the specified number """
    phone_num = request.POST.get("phone_num", "")
    if not phone_num:
        return HttpResponse("No mobile number", content_type="text/plain", status=403)

    pin = _get_pin()

    cache.set(phone_num, pin, 24*3600)

    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                        body="리얼듀 커피 인증 번호 %s" % pin,
                        to="+82%s" %phone_num,
                        from_=settings.TWILIO_FROM_NUMBER,
                    )
    return HttpResponse(u"문자를 발송했습니다.", content_type="text/plain", status=200)



class OrderView(FormView):
    template_name = "order/order.html"
    form_class = OrderForm

    def get_context_data(self, *args, **kwargs):
        beverage = self.kwargs.get("bev", None)
        print(kwargs.get("bev", "none"))

        if beverage == "seogyo":
            price = 4
            title = "서교동 라떼"
            image = get_object_or_404(Image, name="seogyo")
            limit = 20
        elif beverage == "dutch":
            price = 12
            title = "더치 커피"
            image = get_object_or_404(Image, name="dutch")
            limit = 10
        else:
            raise Http404

        context = super(OrderView, self).get_context_data(*args, **kwargs)
        context.update({
            "title": title,
            "form": OrderForm,
            "image": image,
            "total": price,
            "limit": limit,
        })
        return context


    def form_valid(self, form, *args, **kwargs):
        beverage = self.kwargs["bev"]

        order = form.save(commit=False)
        pin = form.cleaned_data.get("pin")
        try:
            pin = int(pin)
        except:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        phone_num = form.cleaned_data.get("phone_regex")

        if _verify_pin(phone_num, pin):
            form.save(commit=False)
        else:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        user, _ = User.objects.get_or_create(phone_number=phone_num)
        reserve_date = form.cleaned_data.get("seperate_date")
        reserve_time = form.cleaned_data.get("seperate_time")
        quantity = form.cleaned_data.get("quantity")


        order.beverage = get_object_or_404(Beverage, name=beverage)

        order.pin = pin
        order.quantity = quantity
        order.reserve_at = datetime(reserve_date.year, reserve_date.month, reserve_date.day, reserve_time.hour, reserve_time.minute, 0 , tzinfo=timezone.get_current_timezone())
        order.user = user

        if beverage == "seogyo":
            price = 12
        elif beverage == "dutch":
            price = 4
        else:
            raise Http404

        order.total_charge = order.quantity * order.beverage.get_price()
        order.save()
        messages.success(self.request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
                            %(order.reserve_at.month, order.reserve_at.day,
                              order.reserve_at.hour, order.reserve_at.minute))
        return super(OrderView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "잘못 입력하셨습니다.")
        return super(OrderView, slef).form_invalid(form, *args, **kwargs)


    def get_success_url(self, *args, **kwargs):
        return reverse("reserve", kwargs={"bev":self.kwargs["bev"]})

    def get(self, request, *args, **kwargs):
        beverage = kwargs.get("bev", None)

        if beverage == "seogyo":
            price = 4
            title = "서교동 라떼"
            image = get_object_or_404(Image, name="seogyo")
            limit = 20
        elif beverage == "dutch":
            price = 12
            title = "더치 커피"
            image = get_object_or_404(Image, name="dutch")
            limit = 10
        else:
            raise Http404

        if request.is_ajax():
            qty = request.GET.get("qty",1)
            try:
                total = int(qty) * price
            except:
                total = None
            data = {
                "total": total,
            }
            return JsonResponse(data)

        form = OrderForm

        ctx = {
            "title": title,
            "form": form,
            "image": image,
            "total": price,
            "limit": limit,
        }

        return render(request, "order/order.html", ctx)




class IdentifyView(FormView):
    template_name = "order/identify.html"
    form_class = IdentifyForm

    def get_context_data(self, *args, **kwargs):
        title = "주문 내역 확인"
        form = IdentifyForm
        image = Image.objects.get(name="icon")

        context = super(IdentifyView, self).get_context_data(*args, **kwargs)

        context.update({
            "title": title,
            "form": form,
            "image": image,
        })
        return context


    def form_valid(self, form, *args, **kwargs):
        phone_num = form.cleaned_data.get("phone_num")
        pin = form.cleaned_data.get("pin")


        user = get_object_or_404(User, phone_number=phone_num)
        orders = Order.objects.filter(user=user).first()

        if orders.pin != pin:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        self.request.session["user_id"] = user.id
        return super(IdentifyView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        response = super(IdentifyView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
        # messages.error(self.request, "잘못 입력하셨습니다.")
        # return self.render_to_response(self.get_context_data())


    def get_success_url(self, *args, **kwargs):
        return reverse("check_order")


    # def get(self, request, *args, **kwargs):
    #     form = IdentifyForm
    #     image = Image.objects.get(name="icon")
    #     title = "주문 내역 확인"
    #     ctx = {
    #         "title": title,
    #         "form": form,
    #         "image":image,
    #     }
    #     return render(request, "order/identify.html",ctx)




class CheckOrderView(ListView):
    template_name = "order/check.html"
    queryset = Order.objects.all()

    def get_queryset(self):
        user_id = self.request.session.get("user_id")
        user = get_object_or_404(User, id=user_id)
        return super(CheckOrderView, self).get_queryset().filter(user=user)


    def post(self, request, *args, **kwargs):

        ctx = {
            "form": "name",
        }
        return render(request, "order/check.html",ctx)


#
# class SeogyoOrderView(FormView):
#     template_name = "order/seogyo_order.html"
#     form_class = SeogyoOrderForm
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(SeogyoOrderView, self).get_context_data(*args, **kwargs)
#         context.update({
#             "title": "서교동 라떼",
#             "form": OrderForm,
#             "image":Image.objects.get(name="dutch"),
#             "total":12,
#         })
#         return context
#
#
#     def form_valid(self, form, *args, **kwargs):
#         order = form.save(commit=False)
#         pin = form.cleaned_data.get("pin")
#         try:
#             pin = int(pin)
#         except:
#             messages.error(self.request, "PIN이 잘못되었습니다.")
#             return self.render_to_response(self.get_context_data())
#
#         phone_num = form.cleaned_data.get("phone_regex")
#
#         if _verify_pin(phone_num, pin):
#             form.save(commit=False)
#         else:
#             messages.error(self.request, "PIN이 잘못되었습니다.")
#             return self.render_to_response(self.get_context_data())
#
#
#         user, _ = User.objects.get_or_create(phone_number=phone_num)
#         reserve_date = form.cleaned_data.get("seperate_date")
#         reserve_time = form.cleaned_data.get("seperate_time")
#         quantity = form.cleaned_data.get("quantity")
#
#         order.quantity = quantity
#         order.reserve_at = datetime(reserve_date.year, reserve_date.month, reserve_date.day, reserve_time.hour, reserve_time.minute, 0 , tzinfo=timezone.get_current_timezone())
#         # order.reserve_at = datetime.combine(reserve_date, reserve_time, tzinfo=timezone.get_current_timezone())
#         order.user = user
#         order.total_charge = order.quantity * 4000
#         order.save()
#         messages.success(self.request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
#                             %(order.reserve_at.month, order.reserve_at.day,
#                               order.reserve_at.hour, order.reserve_at.minute))
#         return super(SeogyoOrderView, self).form_valid(form, *args, **kwargs)
#
#
#     def form_invalid(self, form, *args, **kwargs):
#         messages.error(self.request, "잘못 입력하셨습니다.")
#         return self.render_to_response(self.get_context_data())
#
#
#     def get_success_url(self, *args, **kwargs):
#         return "/order/seogyo/"
#
#     def get(self, request, *args, **kwargs):
#         if request.is_ajax():
#             qty = request.GET.get("qty",1)
#             try:
#                 total = int(qty) * 4
#             except:
#                 total = None
#             data = {
#                 "total": total,
#             }
#             return JsonResponse(data)
#
#
#         form = OrderForm
#         img = Image.objects.get(name="dutch")
#         ctx = {
#             "title": "서교동 라떼",
#             "form": form,
#             "image": img,
#             "total": 4,
#         }
#
#         return render(request, "order/seogyo_order.html", ctx)
