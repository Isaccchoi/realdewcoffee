from django.conf import settings
from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def home(request):
    title = "안녕하세요"

    ctx = {
        "title": title
    }

    return render(request, 'home.html', ctx)


def location(request):
    ctx = {
        "title" : "RealDew Coffee 오시는길",
        "base_lat" : '126.9191396',
        "base_lng" : '37.5551422',
        "naver_client_id" : settings.NAVER_CLIENT_ID,
        "width" : 600,
        "height" : 500,
        "id" : "1007",
    }

    return render(request, 'main/location.html', ctx)
