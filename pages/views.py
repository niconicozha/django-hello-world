from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

# Create your views here.


def home_page_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, World!')
