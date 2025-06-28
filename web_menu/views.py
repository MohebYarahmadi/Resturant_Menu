from django.shortcuts import render
from django.views import generic
from .models import Items

# Class base views


class MenuList(generic.ListView):
    queryset = Items.objects.order_by("-date_created")    # put - to reverse
    template_name = "index.html"


class MenuItemDetail(generic.DetailView):
    model = Items
    template_name = "item_detail.html"
