# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        pass
# полистерол
class PS(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'PS.html')

    def post(self, request, *args, **kwargs):
        pass
# ПВД
class PVD(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        pass
# полипропилен
class PP(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        pass