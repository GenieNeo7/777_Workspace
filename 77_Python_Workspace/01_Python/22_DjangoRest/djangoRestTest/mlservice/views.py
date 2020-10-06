from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import RequestSerializer, serializers 
from .models import Request

# Create your views here.
def index(request):
    return HttpResponse('test')

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
