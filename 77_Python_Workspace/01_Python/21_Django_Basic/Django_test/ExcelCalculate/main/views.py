from django.shortcuts import render, redirect
from . import models
from random import *
from sendEmail.views import *
import hashlib

# Create your views here.

def index(request):
    print('this is the main')
    if 'user_name' in request.session.keys():
        return render(request, 'main/index.html')
    else: 
        return redirect("main_signin")

def signup(request):
    return render(request, 'main/signup.html')

def join(request):
    print('print', request)
    name = request.POST["signupName"]
    email = request.POST["signupEmail"]
    pw = request.POST["signupPW"]    
    # pw encryption
    encoded_pw = pw.encode()
    encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()

    user = models.User()
    user.user_name = name
    user.user_email = email
    user.user_password = encrypted_pw
    user.save()

    code = randint(1000, 9999)
    response = redirect('main_verifyCode')
    response.set_cookie('code', code)
    response.set_cookie('user_id', user.id)
    send_result = send(email, code)
    if send_result:
        return response
    else:
        content = {'message':'이메일 발송 실패.'}
        return render('main/error.html', content)

        # return HttpResponse("이메일 발송 실패")

def signin(request):
    return render(request, 'main/signin.html')

def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    user_code = request.POST["verifyCode"]
    cookie_code = request.COOKIES.get('code')

    if(user_code == cookie_code):
        user = models.User.objects.get(id = request.COOKIES.get('user_id'))
        user.user_validate = 1
        user.save()
        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        # response.set_cookie('user', user)
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return response

    else:
        return redirect('main_verifyCode')

def result(request):
    if 'user_name' in request.session.keys():
        content = {}
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        return render(request, 'main/result.html', content)
    else:
        return redirect('main_signin')

def login(request):
    login_email = request.POST["loginEmail"]
    login_password = request.POST["loginPW"]
    

    try:
        user = models.User.objects.get(user_email=login_email)
    except:
        return redirect('main_loginFail')

    encoded_loginPW = login_password.encode()
    encrypted_loginPW = hashlib.sha256(encoded_loginPW).hexdigest()

    if(encrypted_loginPW == user.user_password):
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email

        return redirect('main_index')
    else:
        return redirect('main_loginFail')

def login_fail(request):
    return render(request, 'main/loginFail.html')

def logout(request):
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_signin')
