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






class DutchOrderForm(forms.ModelForm):
    phone_regex = forms.RegexField(label="휴대폰 번호",
                    help_text="ex)010-1234-5678 형식으로 작성하세요",
                    regex="^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})$",
                    # initial="010-1234-5678",
                    error_messages={
                        'invalid': ("010-1234-5678 형식으로 12자리를 입력하세요.")
                    })
    seperate_time = forms.TimeField(label="예약 시간", input_formats=["%H:%M"],
                                    initial=default_time().strftime("%H:%M"),
                                    widget=forms.TimeInput(attrs={'class': 'time-input'}))
    seperate_date = forms.DateField(label="예약 날짜", input_formats=["%Y-%m-%d"],
                                    help_text="새로 추출을 하기 때문에 24시간 이후로 잡으시는 것을 추천드립니다.",
                                    initial=default_time().strftime("%Y-%m-%d"),
                                    widget=forms.DateInput(attrs={'class': 'date-input'}))

    class Meta:
        model = DutchOrder
        fields = ('quantity',)
        labels = {
            'quantity': _('수량'),
            }


    # def clean(self):
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
