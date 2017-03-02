from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.utils import timezone

# Create your views here.
from datetime import datetime
from datetime import timedelta


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


class DutchOrderView(FormView):
    form_class = DutchOrderForm
    template_name = 'main/dutch_order.html'
    print("-" * 20)


    def form_valid(self, form):
        order = form.save(commit=False)
        print("2" * 20)
        if form.is_valid():
            phone_num = form.cleaned_data.get('phone_regex')
            user, _ = User.objects.get_or_create(phone_number=phone_num)
            print(user.id)
            date = form.cleaned_data.get('seperate_date')
            time = form.cleaned_data.get('seperate_time')
            order.reserve_at = datetime.combine(date,time)
            order.user = user
            order.total_charge = order.quantity * 12000
            order.save()
            return redirect('dutch_order')

        raise Http404


#fixme
