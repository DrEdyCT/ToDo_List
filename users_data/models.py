#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

REMINDER_STATUS = (
        (1, 'new'),
        (2, 'in progress'),
        (3, 'finished'),
    )

class Reminder(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    status = models.IntegerField(choices=REMINDER_STATUS, default=1)