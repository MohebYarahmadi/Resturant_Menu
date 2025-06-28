from django.shortcuts import render
from django.views import generic
from .models import Items

# Class base views


class MenuList(generic.ListView):
    queryset = Items.objects.order_by("-date_created")    # put - to reverse
    template_name = "index.html"

    def get_context_data(self):
        context = {
            "meals": "Pizza",
            "price": 12.22 
        }
        # in index.html file use {{ key }} to get the value
        return context


class MenuItemDetail(generic.DetailView):
    model = Items
    template_name = "item_detail.html"
