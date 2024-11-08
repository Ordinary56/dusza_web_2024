from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
# TODO: add more views
def index(request : HttpRequest) -> HttpResponse:
    return render(request, '/index.html')