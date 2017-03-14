from django.contrib import messages
from django.conf import settings
from django.core import mail

from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils import timezone

from datetime import datetime
from datetime import timedelta
# Create your views here.

from .forms import DutchOrderForm
from .models import User
from .models import DutchOrder
from .models import Image
from .models import MainImage


def home(request):
    greeting = "커피를 사랑하는 리얼듀 커피에 오신것을 환영합니다."
    image = MainImage.objects.filter(active=True).filter(location="main")
    left = MainImage.objects.filter(active=True).get(location="left")
    right = MainImage.objects.filter(active=True).get(location="right")
    a11 = MainImage.objects.get(name="a11")
    b21 = MainImage.objects.get(name="b21")
    b05 = MainImage.objects.get(name="b05")
    loading = MainImage.objects.get(name="loading")

    ctx = {
        "greeting": greeting,
        "images": image,
        "left": left,
        "right": right,
        "a11": a11,
        "b21":b21,
        "loading":loading,
    }

    return render(request, 'main/home.html', ctx)


def aboutus(request):
    ctx = {
        "title": "About Us",
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


class DutchOrderView(View):
    model = Image
    template_name = 'main/dutch_order.html'

    def post(self, request, *args, **kwargs):
        form = DutchOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            phone_num = form.cleaned_data.get('phone_regex')
            user, _ = User.objects.get_or_create(phone_number=phone_num)
            reserve_date = form.cleaned_data.get("seperate_date")
            reserve_time = form.cleaned_data.get("seperate_time")
            quantity = form.cleaned_data.get("quantity")
            emil = form.cleaned_data.get("email")

            order.quantity = quantity
            order.email = email
            order.reserve_at = datetime(reserve_date.year, reserve_date.month, reserve_date.day, reserve_time.hour, reserve_time.minute, 0 , tzinfo=timezone.get_current_timezone())
            # order.reserve_at = datetime.combine(reserve_date, reserve_time, tzinfo=timezone.get_current_timezone())
            order.user = user
            order.total_charge = order.quantity * 12000
            order.save()
            messages.success(request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
                                %(order.reserve_at.month, order.reserve_at.day,
                                  order.reserve_at.hour, order.reserve_at.minute))
            # sendmail(phone_num, quantity, order.reserve_at)
            return redirect('dutch_order')

        raise Http404 # Form이 valid 하지 않을 경우 Http404 일으킴

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
            'form': form,
            'image': img,
            'total': 12,
        }

        return render(request, "main/dutch_order.html", ctx)
