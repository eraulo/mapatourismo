from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

class Tourismo(TemplateView):
    template_name = 'tourismo/index.html'
