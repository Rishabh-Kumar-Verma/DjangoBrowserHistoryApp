# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class URLbox(models.Model):
    url=models.CharField(max_length=250)
