from django.shortcuts import render, redirect
from . import models
from random import *
from sendEmail.views import *

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def signup(request):
    return render(request, 'main/signup.html')

def join(request):
    print('print', request)
    name = request.POST["signupName"]
    email = request.POST["signupEmail"]
    pw = request.POST["signupPW"]    

    user = models.User()
    user.user_name = name
    user.user_email = email
    user.user_password = pw
    user.save()

    code = randint(1000, 9999)
    response = redirect('main_verifyCode')
    response.set_cookie('code', code)
    response.set_cookie('user_id', user.id)
    send_result = send(email, code)
    if send_result:
        return response
    else:
        return HttpResponse("이메일 발송 실패")

def signin(request):
    return render(request, 'main/signin.html')

def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'main/result.html')
