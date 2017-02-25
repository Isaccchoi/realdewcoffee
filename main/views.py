from django.conf import settings
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import Http404

# Create your views here.

from .forms import DutchOrderForm
from .models import User
from .models import DutchOrder


def home(request):
    title = "안녕하세요"

    ctx = {
        "title": title,
    }

    return render(request, 'home.html', ctx)
    # fixme 이미지 슬라이드 기능 추가 필요


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
        # fixme 아이콘 추가
    }

    return render(request, 'main/location.html', ctx)


class DutchOrderView(CreateView):
    form_class = DutchOrderForm
    template_name = "forms.html"

    def form_valid(self, request, *args, **kwargs):
        if form.is_valid():
            phone_num = form.cleaned_data.get('phone_regex', '')
            # if phone_num != '':
#fixme
