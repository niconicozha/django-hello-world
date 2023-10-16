from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from django.views.generic import TemplateView

# Create your views here.


def home_page_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, World!')


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
