from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordChangeForm
from django.contrib.auth import login, load_backend, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse

from accounts.forms import NewUserForm
from routine.models import StudentProfile


def register(request):
    """registering new users into the system"""
    if request.method != 'POST':
        return render(request, 'register.html', {})
    else:
        user_form = NewUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            student_profile = StudentProfile(user=request.POST.get('snumber', False),
                                             student_number=request.POST.get('snumber', False),
                                             first_name=request.POST['fname', False],
                                             last_name=request.POST['lname', False],
                                             email_address=request.POST.get('email', False),
                                             phone_number=request.POST.get('phone', False),
                                             )
