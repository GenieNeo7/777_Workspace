from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mlservice_index(request):
    return HttpResponse('test')