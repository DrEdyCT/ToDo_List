#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from forms import *
from users_data.models import *
from django.contrib.auth.models import User
import datetime

def home_page(request):
    user_authenticated, user_action, go_back_link = login_status(request)
    return render(request, 'home_page.html', locals())

def registration(request):
    user_authenticated, user_action, go_back_link = login_status(request)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data['password']
            pass2 = form.cleaned_data['password2']
            username = form.cleaned_data['login']
            email = form.cleaned_data['email']
            if pass1 != pass2:
                error = 'Passwords do not match'
                return render(request, 'registration_page.html', locals())
            new_user = User.objects.create_user(username, email, pass1)
            new_user.save()
            return render(request, 'congratulate.html', locals())
    else:
        form = RegistrationForm()
    return render(request, 'registration_page.html', locals())

def todo_list(request):
    user_authenticated, user_action, go_back_link = login_status(request)
    form = MainForm(request.POST)
    if form.is_valid():
        rimind = form.cleaned_data['text']
        my_date = form.cleaned_data['date']
        if rimind:
            id = request.user.id
            text = Reminder.objects.all()
            text.create(text = rimind, user_id = id, date = my_date)
    reminders = Reminder.objects.filter(user_id=request.user.id).order_by('date')
    new_reminders = reminders.filter(status=1)
    in_progress_reminders = reminders.filter(status=2)
    finished_reminders = reminders.filter(status=3)
    return render(request, 'to_do_list_page.html', locals())

def delete_action(request, offset):
    text = Reminder.objects.filter(id=offset)
    text.delete()
    return redirect('/my_todo_list')

def done_action(request, offset):
    text = Reminder.objects.filter(id=offset)
    text.update(status=3)
    return redirect('/my_todo_list')

def undone_action(request, offset):
    text = Reminder.objects.filter(id=offset)
    text.update(status=1)
    return redirect('/my_todo_list')

def in_progress_action(request, offset):
    text = Reminder.objects.filter(id=offset)
    text.update(status=2)
    return redirect('/my_todo_list')

def edit_text(request, offset):
    user_authenticated, user_action, go_back_link = login_status(request)
    data = Reminder.objects.filter(id=offset)[0]
    date = datetime.datetime.strptime(data.date, "%d.%m.%Y")
    if request.method == 'POST':
        form = EditReminderTextForm(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data['text']
            new_date = form.cleaned_data['date']
            old_reminder = Reminder.objects.filter(id=offset)
            old_reminder.update(text=new_text, date=new_date)
            return redirect('/my_todo_list')
    else:
        form = EditReminderTextForm(
            initial = {
                'text': data.text,
                'date': date.strftime("%Y-%m-%d"),
            }
        )
    return render(request, 'redact_page.html', locals())

def signin(request):
    user_authenticated, user_action, go_back_link = login_status(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            name = form.cleaned_data['login']
            if '@' not in name:
                user = authenticate(username = name, password = password)
            else:
                a = User.objects.filter(email=name)[0].username
                user = authenticate(username = a, password = password)
            if len(User.objects.all()) == 0 or user is None:
                error = 'E-mail or password is invalid'
            else:
                for i in User.objects.all():
                    if user.username != i.username or user.email != i.email:
                        error = 'E-mail or password is invalid'
                    elif user.password != i.password:
                        error = 'E-mail or password is invalid'
                    else:
                        form = MainForm()
                        login(request, user)
                        return redirect('/my_todo_list')
            return render(request, 'signin_page.html', locals())
    else:
        form = LoginForm()
    return render(request, 'signin_page.html', locals())

def login_status(request):
    go_back_link = request.META.get('HTTP_REFERER', '')
    if request.user.is_authenticated():
        user_authenticated = True
        user_action = "/signout/"
    else:
        user_authenticated = False
        user_action = "/signin/"
    return [user_authenticated, user_action, go_back_link]

def signout(request):
    logout(request)
    return home_page(request)

def go_to_todo_list(request):
    user_authenticated, user_action, go_back_link = login_status(request)
    if user_authenticated:
        return redirect('/my_todo_list')
    else:
        return signin(request)