import hashlib
import re
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import UserInfo


def login(request):
    request.COOKIES['url'] = request.get_full_path()
    return render(request, "user/login.html")


def login_handle(request):
    email = request.POST.get('email')
    user = UserInfo.objects.filter(email=email).first()
    if user:
        if request.POST.get('password') == user.password:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            if request.POST.get('remember') is None:
                request.session.set_expiry(0)
            return redirect(request.COOKIES.get('url', '/index/'))
    response = HttpResponseRedirect('/user/login/')
    response.set_cookie('message', 'login_failed', 300)
    return response


def logout(request):
    request.session.flush()
    return redirect('/index/')


def register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    response = HttpResponseRedirect('/user/login/')

    if 0 < len(name) <= 20 and 5 < len(password) and re.match(r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}', email) and not UserInfo.objects.filter(email=email):
        sha1 = hashlib.sha1()
        sha1.update(password.encode('utf-8'))
        password_hash = sha1.hexdigest()
        user_info = UserInfo(name=name, email=email, password=password_hash)
        user_info.save()
        response.set_cookie('message', 'register_successful', 30)
    else:
        response.set_cookie('message', 'register_failed', 30)
    return response
