import random

from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.utils import timezone

from datetime import datetime

# Create your views here.

from main.models import Image
from .models import User
from .models import DutchOrder
from .models import SeogyodongOrder
from .forms import DutchOrderForm
from .forms import SeogyoOrderForm

from twilio.rest import TwilioRestClient


def _get_pin(length=5):
    return random.sample((range(10**(length-1), 10**length), 1)[0], 1)


def _verify_pin(phone_num, pin):
    print(pin)
    print(cache.get(phone_num)[0])
    return pin == cache.get(phone_num)[0]


def ajax_send_pin(request):
    """ Sends SMS PIN to the specified number """
    phone_num = request.POST.get('phone_num', "")
    if not phone_num:
        return HttpResponse("No mobile number", content_type='text/plain', status=403)

    pin = _get_pin()

    cache.set(phone_num, pin, 24*3600)

    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                        body="리얼듀 커피 인증 번호 %s" % pin,
                        to="+82%s" %phone_num,
                        from_=settings.TWILIO_FROM_NUMBER,
                    )
    return HttpResponse(u"문자를 발송했습니다.", content_type='text/plain', status=200)



class DutchOrderView(FormView):
    template_name = "order/dutch_order.html"
    form_class = DutchOrderForm

    def get_context_data(self, *args, **kwargs):
        context = super(DutchOrderView, self).get_context_data(*args, **kwargs)
        context.update({
            "title": "Dutch Coffee",
            "form": DutchOrderForm,
            "image":Image.objects.get(name="dutch"),
            "total":12,
        })
        return context


    def form_valid(self, form, *args, **kwargs):
        order = form.save(commit=False)
        pin = form.cleaned_data.get('pin')
        try:
            pin = int(pin)
        except:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        phone_num = form.cleaned_data.get('phone_regex')

        if _verify_pin(phone_num, pin):
            form.save(commit=False)
        else:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        user, _ = User.objects.get_or_create(phone_number=phone_num)
        reserve_date = form.cleaned_data.get("seperate_date")
        reserve_time = form.cleaned_data.get("seperate_time")
        quantity = form.cleaned_data.get("quantity")

        order.quantity = quantity
        order.reserve_at = datetime(reserve_date.year, reserve_date.month, reserve_date.day, reserve_time.hour, reserve_time.minute, 0 , tzinfo=timezone.get_current_timezone())
        order.user = user
        order.total_charge = order.quantity * 12000
        order.save()
        messages.success(self.request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
                            %(order.reserve_at.month, order.reserve_at.day,
                              order.reserve_at.hour, order.reserve_at.minute))
        return super(DutchOrderView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "잘못 입력하셨습니다.")
        return self.render_to_response(self.get_context_data())


    def get_success_url(self, *args, **kwargs):
        return "/order/dutch"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            qty = request.GET.get("qty",1)
            try:
                total = int(qty) * 12
            except:
                total = None
            data = {
                'total': total,
            }
            return JsonResponse(data)


        form = DutchOrderForm
        img = Image.objects.get(name="dutch")
        ctx = {
            'title': "Dutch Coffee",
            'form': form,
            'image': img,
            'total': 12,
        }

        return render(request, "order/dutch_order.html", ctx)


class SeogyoOrderView(FormView):
    template_name = "order/seogyo_order.html"
    form_class = SeogyoOrderForm

    def get_context_data(self, *args, **kwargs):
        context = super(SeogyoOrderView, self).get_context_data(*args, **kwargs)
        context.update({
            "title": "서교동 커피",
            "form": DutchOrderForm,
            "image":Image.objects.get(name="dutch"),
            "total":12,
        })
        return context


    def form_valid(self, form, *args, **kwargs):
        order = form.save(commit=False)
        pin = form.cleaned_data.get('pin')
        try:
            pin = int(pin)
        except:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        phone_num = form.cleaned_data.get('phone_regex')

        if _verify_pin(phone_num, pin):
            form.save(commit=False)
        else:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())


        user, _ = User.objects.get_or_create(phone_number=phone_num)
        reserve_date = form.cleaned_data.get("seperate_date")
        reserve_time = form.cleaned_data.get("seperate_time")
        quantity = form.cleaned_data.get("quantity")

        order.quantity = quantity
        order.reserve_at = datetime(reserve_date.year, reserve_date.month, reserve_date.day, reserve_time.hour, reserve_time.minute, 0 , tzinfo=timezone.get_current_timezone())
        # order.reserve_at = datetime.combine(reserve_date, reserve_time, tzinfo=timezone.get_current_timezone())
        order.user = user
        order.total_charge = order.quantity * 4000
        order.save()
        messages.success(self.request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
                            %(order.reserve_at.month, order.reserve_at.day,
                              order.reserve_at.hour, order.reserve_at.minute))
        return super(SeogyoOrderView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "잘못 입력하셨습니다.")
        return self.render_to_response(self.get_context_data())


    def get_success_url(self, *args, **kwargs):
        return "/order/seogyo/"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            qty = request.GET.get("qty",1)
            try:
                total = int(qty) * 4
            except:
                total = None
            data = {
                'total': total,
            }
            return JsonResponse(data)


        form = DutchOrderForm
        img = Image.objects.get(name="dutch")
        ctx = {
            "title": "서교동 커피",
            "form": form,
            "image": img,
            "total": 4,
        }

        return render(request, "order/seogyo_order.html", ctx)
