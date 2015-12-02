#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from users_data.models import *
from forms import *
from django.contrib.auth.models import User

def email_validate(value):
    for i in User.objects.all():
        if value == i.email:
            raise ValidationError('E-mail already exist')

def login_validate(value):
    for i in User.objects.all():
        if value == i.username:
            raise ValidationError('Login already exist')

def pass_validate(value):
    if len(value) < 6:
        raise ValidationError('Password must be more than 6 symbols')