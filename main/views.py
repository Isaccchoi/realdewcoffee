from django.conf import settings
from django.core import mail

from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from .models import MainImage
from .models import Image



def home(request):
    greeting = "커피를 사랑하는 리얼듀 커피에 오신것을 환영합니다."
    image = MainImage.objects.filter(active=True).filter(location="main")
    # left = MainImage.objects.filter(active=True).get(location="left")
    # right = MainImage.objects.filter(active=True).get(location="right")
    a11 = MainImage.objects.get(name="a11")
    b21 = MainImage.objects.get(name="b21")
    b05 = MainImage.objects.get(name="b05")
    loading = MainImage.objects.get(name="loading")
    icon = Image.objects.get(name="icon")

    ctx = {
        "greeting": greeting,
        "images": image,
        # "left": left,
        # "right": right,
        "a11": a11,
        "b21":b21,
        "b05":b05,
        "loading":loading,
        "icon": icon,
    }

    return render(request, 'main/home.html', ctx)


def aboutus(request):
    title = "About us"
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
        'working_time': "09:00 ~ 23:00",
        'phone': "02-333-5945"
    }

    return render(request, 'main/location.html', ctx)
