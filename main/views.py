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
        "title" : "RealDew Coffee",
        "base_lat" : '126.919122',
        "base_lng" : '37.555112',
        "naver_client_id" : settings.NAVER_CLIENT_ID,
        "width" : 800,
        "height" : 600,
        "id" : "1007",
    }

    return render(request, 'main/location.html', ctx)
