from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from datetime import timedelta

from .models import DutchOrder


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
    if value == "010-1234-5678":
        raise forms.ValidationError('전화번호를 확인하세요.')




class DutchOrderForm(forms.ModelForm):
    seperate_time = forms.TimeField(label="예약 시간", input_formats=["%H:%M"],
                                    initial=default_time().strftime("%H:%M"),
                                    widget=forms.TimeInput(attrs={'class': 'time-input'}))
    seperate_date = forms.DateField(label="예약 날짜", input_formats=["%Y-%m-%d"],
                                    help_text="새로 추출을 하기 때문에 24시간 이후로 잡으시는 것을 추천드립니다.",
                                    initial=default_time().strftime("%Y-%m-%d"),
                                    widget=forms.DateInput(attrs={'class': 'date-input'}))

    phone_regex = forms.RegexField(label="휴대폰 번호",
                    regex="^01([0|1|6|7|8|9]?)([0-9]{3,4})([0-9]{4})$",
                    # initial="010-1234-5678",
                    error_messages={
                        'invalid': ("010-1234-5678 형식으로 12자리를 입력하세요.")
                        },
                    validators = [validate_phone_regex],
                    )
    pin = forms.IntegerField(label="PIN",
                    error_messages={
                        'invalid': ("PIN이 일치하지 않습니다."),
                        },
                    required=True,
                    )

    class Meta:
        model = DutchOrder
        fields = ('quantity',)
        labels = {
            'quantity': _('수량'),
            }

    # def clean_phone_regex(self):
    #     phone_regex = self.cleaned_data['phone_regex']
    #     if phone_regex == "010-1234-5678":
    #         raise forms.ValidationError("올바른 번호를 입력하세요.")
    #     return phone_regex
    # # def clean(self):
    #     cleaned_data = super(DutchOrderForm, self).clean()
    #     reserve_date = cleaned_data['seperate_date']
    #     reserve_time = cleaned_data['seperate_time']
    #
    #     self.cleaned_data['reserve_at'] = datetime.combine(reserve_date, reserve_time)
    #
    #     # self.cleaned_data['reserve_at'] = \
    #     #                 datetime.combine(self.cleaned_data.get('seperate_date', None),
    #     #                                     self.cleaned_data.get('seperate_time',None))
    #     if self.cleaned_data['reserve_at'] < default_time:
    #         raise ValidationError("예약 가능 시간이 아닙니다. %s 이후로 예약해주세요") %(default_time)
