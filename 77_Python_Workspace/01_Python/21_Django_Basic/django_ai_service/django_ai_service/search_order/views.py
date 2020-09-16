from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'search_order/index.html') 

def searchRequest(request):
    return HttpResponse('hello django')