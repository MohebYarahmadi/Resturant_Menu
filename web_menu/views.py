from django.shortcuts import render
from django.views import generic
from .models import Items, MEAL_TYPE, STATUS

# Class base views


class MenuList(generic.ListView):
    queryset = Items.objects.order_by("-date_created")    # put - to reverse
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Items
    template_name = "item_detail.html"
