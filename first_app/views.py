from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def result(request):
    return HttpResponse("This is result pagess")
def home(request):
    return HttpResponse("this is first app home page")