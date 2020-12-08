from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Page


# Create your views here


class HomePageView(ListView):
    model = Page
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


