import random

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from restaurants.models import RestaurantLocation
from django.views.generic import TemplateView, ListView, DetailView


# def home(request):
#     num = None
#     some_list = [
#         random.randint(0, 100000000),
#         random.randint(0, 100000000),
#         random.randint(0, 100000000)
#     ]
#     condition_bool_item = False
#     if condition_bool_item:
#         num = random.randint(0, 100000000)
#     context = {
#         "num": num,
#         "some_list": some_list
#     }
#     return render(request, "home.html", context)
#
#
# def about(request):
#     context = {
#     }
#     return render(request, "about.html", context)
#
#
# def contact(request):
#     context = {
#     }
#     return render(request, "contact.html", context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        # context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 100000000),
            random.randint(0, 100000000),
            random.randint(0, 100000000)
        ]
        condition_bool_item = False
        if condition_bool_item:
            num = random.randint(0, 100000000)
        context = {
            "num": num,
            "some_list": some_list
        }
        print(context)
        return context


# def restaurant_listview(request):
#     template_name = "restaurants/restaurants_list.html"
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, template_name, context)

class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    template_name = "restaurants/restaurantlocation_list.html"


class SearchRestaurantListView(ListView):  # For all ListView context variable is always object_list
    # template_name = "restaurants/restaurantlocation_list.html" # This template is running for this class
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        print(queryset)
        return queryset


class RestaurantDetailView(DetailView):  # For all DetailView context variable is always object
    # queryset = RestaurantLocation.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super(RestaurantDetailView, self).get_context_data(**kwargs)
    #     print('-----------------------')
    #     print(self.kwargs)
    #     print('-----------------------')
    #     print(context)
    #     return context

    def get_object(self, *args,**kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id) # or pk=rest_id
        return obj

# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
