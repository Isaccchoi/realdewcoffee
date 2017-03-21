from django.shortcuts import render
from django.views.generic.edit import FormView

# Create your views here.

from main.models import Image
from .models import DutchOrder
from .models import SeogyodongOrder
from .forms import DutchOrderForm




class DutchOrderView(FormView):
    template_name = "order/order.html"
    form_class = DutchOrderForm

    def get_context_data(self, *args, **kwargs):
        context = super(DutchOrderView, self).get_context_data(*args, **kwargs)
        context.update({
            "form": DutchOrderForm,
            "image":Image.objects.get(name="dutch"),
            "total":12,
        })
        return context


    def form_valid(self, form, *args, **kwargs):
        order = form.save(commit=False)
        pin = form.cleaned_data.get('pin')
        try:
            pin = int(pin)
        except:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        phone_num = form.cleaned_data.get('phone_regex')
        print(phone_num)
        print(pin)
        # verify = self.request.POST.get("verify_phone", "")
        # if not verify:
        #     return super(DutchOrderView, self).form_invalid(form, *args, **kwargs)

        if _verify_pin(phone_num, pin):
            form.save(commit=False)
        else:
            messages.error(self.request, "PIN이 잘못되었습니다.")
            return self.render_to_response(self.get_context_data())

        user, _ = User.objects.get_or_create(phone_number=phone_num)
        reserve_date = form.cleaned_data.get("seperate_date")
        reserve_time = form.cleaned_data.get("seperate_time")
        quantity = form.cleaned_data.get("quantity")

        order.quantity = quantity
        order.reserve_at = datetime(reserve_date.year, reserve_date.month, reserve_date.day, reserve_time.hour, reserve_time.minute, 0 , tzinfo=timezone.get_current_timezone())
        # order.reserve_at = datetime.combine(reserve_date, reserve_time, tzinfo=timezone.get_current_timezone())
        order.user = user
        order.total_charge = order.quantity * 12000
        order.save()
        messages.success(self.request, "%s월%s일 %s시 %s분으로 예약이 완료되었습니다."\
                            %(order.reserve_at.month, order.reserve_at.day,
                              order.reserve_at.hour, order.reserve_at.minute))
        return super(DutchOrderView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "잘못 입력하셨습니다.")
        return self.render_to_response(self.get_context_data())


    def get_success_url(self, *args, **kwargs):
        return "/order/"

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

        return render(request, "order/order.html", ctx)
