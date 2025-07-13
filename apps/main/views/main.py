# -*- coding: utf-8 -*-
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views import View

class MainView(View):
    """Main page handler (/)"""
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, 'main.html')
