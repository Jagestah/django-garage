# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class doorLog(models.Model):
    door_log = models.CharField(max_length=200)
    log_timestamp = models.DateTimeField('Logged at')
    def __str__(self):
        return self.door_log
