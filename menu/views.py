from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here

from .models import Beverage
from .models import Category


class MenuListView(ListView):
    model = Category
    template_name = "menu/menu_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MenuListView, self).get_context_data(*args, **kwargs)
        context["coffees"] = Category.objects.get(name="Coffee").beverage_set.all()
        context["teas"] = Category.objects.get(name="Tea").beverage_set.all()
        context["others"] = Category.objects.get(name="Others").beverage_set.all()
        return context



class MenuDetailView(DetailView):
    model = Category
    template_name = "menu/menu_detail.html"
    context_object_name = "details"
    slug_url_kwargs = "not_slug"

    def get_queryset(self):
        beverage = Beverage.objects.filter(slug=self.kwargs['slug'])
        if beverage == None:
            raise Http404

        return beverage
