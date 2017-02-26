from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from .models import DutchOrder

class DutchOrderForm(forms.ModelForm):
    phone_regex = forms.RegexField(label="연락처",
                    regex="^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$",
                    error_message="010-1234-5678 형식으로 10~12자리를 입력하세요.")

    class Meta:
        model = DutchOrder
        fields = ('reserve_at', 'quantity',)
        labels = {
            'reserve_at': _('예약 시간'),
            'quantity': _('수량'),
            }
