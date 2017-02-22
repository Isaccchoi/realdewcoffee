from django.conf import settings
from django.shortcuts import render

# Create your views here.



def home(request):
    title = "안녕하세요"

    ctx = {
        "title": title,
    }

    return render(request, 'home.html', ctx)


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
        'working_time': "08:00 ~ 23:00",
        'phone': "02-333-5945"
        # fixme
    }

    return render(request, 'main/location.html', ctx)
