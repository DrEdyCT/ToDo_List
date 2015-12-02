#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms.extras import SelectDateWidget

from users_data.models import *
from validators import *
from django import forms
from django.forms import ModelForm, Form

class RegistrationForm(Form):
    email = forms.EmailField(
        label='',
        error_messages={'required': 'Email is required'},
        validators=[email_validate],
        widget=forms.TextInput(attrs={'type':'email', 'class':'form-control', 'placeholder':'E-mail'}),
    )
    login = forms.CharField(
        label='',
        error_messages={'required': 'Login is required'},
        validators=[login_validate],
        widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Login'}),
    )
    password = forms.CharField(
        label='',
        error_messages={'required': 'Password is required'},
        validators=[pass_validate],
        widget=forms.TextInput(attrs={'type':'password', 'class':'form-control', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label='',
        error_messages={'required': 'Repeat password'},
        validators=[pass_validate],
        widget=forms.TextInput(attrs={'type':'password', 'class':'form-control', 'placeholder':'Repeat password'}),
    )

class LoginForm(Form):
    login = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Login or e-mail'})
    )
    password = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'type':'password', 'class':'form-control', 'placeholder':'Password'})
    )

class MainForm(Form):
    text = forms.CharField(
        label='Text of task:',
        widget=forms.Textarea(attrs={'type':'text', 'class':'form-control', 'rows':'3'}),
        required=False
    )
    date = forms.CharField(
        label='Lead time:',
        widget=forms.DateTimeInput(attrs={'type':'date', 'class':'form-control'}),
        required=False,
    )

class EditReminderTextForm(Form):
    text = forms.CharField(
        label='Text of task:',
        error_messages={'required': 'Enter text of task'},
        widget=forms.Textarea(attrs={'type':'text', 'class':'form-control', 'rows':'3'}),
        initial='',
    )
    date = forms.CharField(
        label='Lead time:',
        widget=forms.DateTimeInput(attrs={'type':'date', 'class':'form-control', 'id':'datepicker'}),
        required=False,
    )