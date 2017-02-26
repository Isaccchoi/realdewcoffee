from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from .models import DutchOrder

class DutchOrderForm(forms.ModelForm):
    phone_regex = forms.RegexField(label="연락처",
                    regex="^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})$",
                    error_message={
                        'invalid': ("010-1234-5678 형식으로 10~12자리를 입력하세요.")
                    }
                )

    class Meta:
        model = DutchOrder
        fields = ('reserve_at','quantity',)
        labels = {
            'reserve_at': _('예약 시간'),
            'quantity': _('수량'),
            }
# 기본적인 기능 구현 완료 regex를 좀 더 명확하게 정할 필요가 있음
# datetimefield 입력시 좀 더 편하게 구현할 방법을 찾아야함
#
