from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from datetime import timedelta

from .models import Order
# from .models import SeogyodongOrder


def default_time():
    now = timezone.now()
    open = now.replace(hour=9, minute=0, second=0, microsecond=0,
                            tzinfo=timezone.get_current_timezone())
    close = now.replace(hour=21, minute=0, second=0, microsecond=0,
                            tzinfo=timezone.get_current_timezone())
    if now < close:
        able_time = open + timedelta(days=1)
    else:
        able_time = open + timedelta(days=2)
    return able_time


def validate_phone_regex(value):
    if value == "01012345678":
        raise forms.ValidationError('전화번호를 확인하세요.')




class OrderForm(forms.ModelForm):
    seperate_time = forms.TimeField(label="예약 시간",
                                    input_formats=["%H:%M"],
                                    initial=default_time().strftime("%H:%M"),
                                    widget=forms.TimeInput(attrs={'class': 'time-input'}))
    seperate_date = forms.DateField(label="예약 날짜",
                                    input_formats=["%Y-%m-%d"],
                                    help_text="새로 추출을 하기 때문에 24시간 이후로 잡으시는 것을 추천드립니다.",
                                    initial=default_time().strftime("%Y-%m-%d"),
                                    widget=forms.DateInput(attrs={'class': 'date-input'}))

    phone_regex = forms.RegexField(label="휴대폰 번호",
                    regex="^01([0|1|6|7|8|9]?)([0-9]{7,8})$",
                    # initial="010-1234-5678",
                    error_messages={
                        'invalid': ("01012345678 형식으로 10~11자리를 입력하세요.")
                        },
                    help_text="01012345678 형식으로 작성하세요.",
                    validators = [validate_phone_regex],
                    widget=forms.TextInput(attrs={'placeholder':'01012345678'}),
                    )
    pin = forms.IntegerField(label="PIN",
                    error_messages={
                        'invalid': ("PIN이 일치하지 않습니다."),
                        },
                    required=True,
                    )

    class Meta:
        model = Order
        fields = ('quantity',)
        labels = {
            'quantity': _('수량'),
            }


class IdentifyForm(forms.Form):
    phone_num = forms.RegexField(label="휴대폰 번호",
                    regex="^01([0|1|6|7|8|9]?)([0-9]{7,8})$",
                    error_messages={
                        'invalid': ("01012345678 형식으로 10~11자리를 입력하세요.")
                        },
                    validators = [validate_phone_regex],
                    help_text="010123456787 형식으로 작성하세요.",
                    widget=forms.TextInput(attrs={'placeholder':'01012345678'}),
                )
    pin = forms.IntegerField(label="PIN",
                    help_text="주문시 받았던 PIN을 입력하세요.",
                    error_messages = {
                        "invalid" :("PIN이 일치하지 않습니다."),
                    },
                    required=True,
                )
