import random

from django import forms
from django.contrib import messages
from django.conf import settings
from django.core import mail
from django.core.cache import cache

from django.http import Http404
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils import timezone

from datetime import datetime
from datetime import timedelta
# Create your views here.

# from .forms import DutchOrderForm
from .models import User
# from .models import DutchOrder
from .models import Image
from .models import MainImage

from twilio.rest import TwilioRestClient


def home(request):
    greeting = "커피를 사랑하는 리얼듀 커피에 오신것을 환영합니다."
    image = MainImage.objects.filter(active=True).filter(location="main")
    # left = MainImage.objects.filter(active=True).get(location="left")
    # right = MainImage.objects.filter(active=True).get(location="right")
    a11 = MainImage.objects.get(name="a11")
    b21 = MainImage.objects.get(name="b21")
    b05 = MainImage.objects.get(name="b05")
    loading = MainImage.objects.get(name="loading")

    ctx = {
        "greeting": greeting,
        "images": image,
        # "left": left,
        # "right": right,
        "a11": a11,
        "b21":b21,
        "b05":b05,
        "loading":loading,
    }

    return render(request, 'main/home.html', ctx)


def aboutus(request):
    title = "About Us"
    image = MainImage.objects.filter(active=True).filter(location="main")
    # left = MainImage.objects.filter(active=True).get(location="left")
    # right = MainImage.objects.filter(active=True).get(location="right")
    a11 = MainImage.objects.get(name="a11")
    b21 = MainImage.objects.get(name="b21")
    b05 = MainImage.objects.get(name="b05")
    loading = MainImage.objects.get(name="loading")

    ctx = {
        "title": title,
        "images": image,
        # "left": left,
        # "right": right,
        "a11": a11,
        "b21":b21,
        "b05":b05,
        "loading":loading,
    }
    return render(request, 'about.html', ctx)



def location(request):
    ctx = {
        "title" : "Location",
        "base_lat" : '126.919122',
        "base_lng" : '37.555112',
        "naver_client_id" : settings.NAVER_CLIENT_ID,
        "height" : 600,
        "id" : "1007",
        'address': "서울특별시 마포구 월드컵북로1길 26-17",
        'address_short': "서울특별시 마포구 서교동 352-7",
        'working_time': "09:00 ~ 21:00",
        'phone': "02-333-5945"
    }

    return render(request, 'main/location.html', ctx)



# def sendmail(phone, qty,reserve_at):
#     connection = mail.get_connection()
#     connection.open()
#     email = mail.EmailMessage(
#         "Dutch reservation",
#         "%s월 %s일 %s시 %s분 더치 %s병 예약, 연락처: %s"\
#                 %(reserve_at.month, reserve_at.day, reserve_at.hour,
#                 reserve_at.minute, qty, phone),
#         "realdew@naver.com",
#         to = ("isaccchoi@naver.com","beredfaced@naver.com"),
#     )
#     email.send()
#     connection.close()


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





# class DutchOrderView(FormView):
#     template_name = "main/dutch_order.html"
#     form_class = DutchOrderForm
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(DutchOrderView, self).get_context_data(*args, **kwargs)
#         context.update({
#             "form": DutchOrderForm,
#             "image":Image.objects.get(name="dutch"),
#             "total":12,
#         })
#         return context
#
#
#     def form_valid(self, form, *args, **kwargs):
#         order = form.save(commit=False)
#         pin = form.cleaned_data.get('pin')
#         try:
#             pin = int(pin)
#         except:
#             messages.error(self.request, "PIN이 잘못되었습니다.")
#             return self.render_to_response(self.get_context_data())
#
#         phone_num = form.cleaned_data.get('phone_regex')
#         print(phone_num)
#         print(pin)
#         # verify = self.request.POST.get("verify_phone", "")
#         # if not verify:
#         #     return super(DutchOrderView, self).form_invalid(form, *args, **kwargs)
#
#         if _verify_pin(phone_num, pin):
#             form.save(commit=False)
#         else:
#             messages.error(self.request, "PIN이 잘못되었습니다.")
#             return self.render_to_response(self.get_context_data())
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
#         order.total_charge = order.quantity * 12000
#         order.save()
#         messages.success(self.request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
#                             %(order.reserve_at.month, order.reserve_at.day,
#                               order.reserve_at.hour, order.reserve_at.minute))
#         return super(DutchOrderView, self).form_valid(form, *args, **kwargs)
#
#
#     def form_invalid(self, form, *args, **kwargs):
#         messages.error(self.request, "잘못 입력하셨습니다.")
#         return self.render_to_response(self.get_context_data())
#
#
#     def get_success_url(self, *args, **kwargs):
#         return "/order/"
#
#     def get(self, request, *args, **kwargs):
#         if request.is_ajax():
#             qty = request.GET.get("qty",1)
#             try:
#                 total = int(qty) * 12
#             except:
#                 total = None
#             data = {
#                 'total': total,
#             }
#             return JsonResponse(data)
#
#
#         form = DutchOrderForm
#         img = Image.objects.get(name="dutch")
#         ctx = {
#             'form': form,
#             'image': img,
#             'total': 12,
#         }
#
#         return render(request, "main/dutch_order.html", ctx)
