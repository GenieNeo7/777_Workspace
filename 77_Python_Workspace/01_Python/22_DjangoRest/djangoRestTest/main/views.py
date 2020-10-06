from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_main(request):
    content = {'data' : '292513'}
    return render(request, 'main/index.html', content)
