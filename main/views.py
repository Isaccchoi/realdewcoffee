from django.conf import settings
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView

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
        'working_time': "09:00 ~ 21:00",
        'phone': "02-333-5945"
        # fixme 아이콘 추가
    }

    return render(request, 'main/location.html', ctx)


# class AjaxableResponseMixin(object):
#     def form_invalid(self, form):
#         response = super(AjaxableResponseMixin, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         return reponse
#
#     def form_valid(self, form):
#         response = super(AjaxableResponseMixin, self).form_valid(form)
#         if self.request.is_ajax():
#             qty = self.request.GET.get("qty", 1)
#             qty = int(qty)
#             price = 12000
#             total = qty * price
#             data = {
#                 'total': total,
#             }
#             print("-"*50)
#             return JsonResponse(data)
#
#         return response


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
            order.quantity = quantity
            order.reserve_at = datetime.combine(reserve_date, reserve_time)
            order.user = user
            order.total_charge = order.quantity * 12000
            order.save()
            return redirect('dutch_order')
            # fixme 완료시 Home으로 Redirect시키며 FlashMessage 보내주면 좋을듯
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
# class DutchOrderView(AjaxableResponseMixin, FormView):
#     form_class = DutchOrderForm
#     template_name = 'main/dutch_order.html'
#     model = Image
#
#
#     def get_queryset(self):
#         img = Image.objects.get(name="dutch")
#
#
#     def form_valid(self, form):
#         order = form.save(commit=False)
#         if form.is_valid():
#             phone_num = form.cleaned_data.get('phone_regex')
#             user, _ = User.objects.get_or_create(phone_number=phone_num)
#             reserve_date = form.cleaned_data.get("seperate_date")
#             reserve_time = form.cleaned_data.get("seperate_time")
#             quantity = form.cleaned_date.get("quantity")
#             order.quantity = quantity
#             order.reserve_at = datetime.combine(reserve_date, reserve_time)
#             order.user = user
#             order.total_charge = order.quantity * 12000
#             order.save()
#             return redirect('dutch_order')
#
#         raise Http404


#fixme
