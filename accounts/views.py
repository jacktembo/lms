from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordChangeForm
from django.contrib.auth import login, load_backend, authenticate, logout, update_session_auth_hash
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse

from accounts.forms import NewUserForm
from routine.models import StudentProfile


def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        form = User()
        form.username = request.POST.get('snumber', False)
        form.first_name = request.POST.get('fname', False)
        form.last_name = request.POST.get('lname', False)
        form.email = request.POST.get('email')
        form.password1 = request.POST.get('password', False)
        form.password2 = request.POST.get('password', False)
        try:
            form.save()
        except IntegrityError:
            return HttpResponse('user already exist')

        user = User.objects.get(username=form.username)
        user.set_password(form.password1)
        user.save()
        return HttpResponse('THANKS')


def login_view(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        username = request.POST.get('snumber', False)
        password = request.POST.get('login-password', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('logged in')
        else:
            return HttpResponse('incorrect username or password')

def dashboard(request):
    return HttpResponse('Dashboard')