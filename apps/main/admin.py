# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.main import models

admin.site.register(models.Partner)
admin.site.register(models.PP)
admin.site.register(models.PS)
admin.site.register(models.PVD)
# Register your models here.
