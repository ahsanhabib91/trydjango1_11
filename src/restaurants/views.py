import random

from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView


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
        context = super(HomeView, self).get_context_data(*args, **kwargs)
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


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
