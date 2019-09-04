# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from django.core.mail import send_mail



class MainView(View):
    """Main page handler (/)"""
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')

    def post(self, request, *args, **kwargs):
        pass

class ProductView(View):
    """Base class for product handlers"""
    
    page = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.page)

    def post(self, request, *args, **kwargs):
        pass

class PSView(ProductView):
    """Polystyrene page handler (/ps)"""
    
    page = 'PS.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.page)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        phone = request.POST.get('phone number')
        product_id = request.POST.get('id')
        name = request.POST.get('name')
        
        send_mail(
            'Subject',
        'Email message',
        'vinat.supp0t@yandex.ru',
        ["lavr3x@rambler.ru"],
        fail_silently=False,
        )


        return render(request, self.page)

class PVDView(ProductView):
    """PVD page handler (/pvd)"""
    def get(self, request, *args, **kwargs):
        return render(request, self.page)

    def post(self, request, *args, **kwargs):
        pass

class PPView(ProductView):
    """polypropylene page handler (/pp)"""
    def get(self, request, *args, **kwargs):
        return render(request, self.page)

    def post(self, request, *args, **kwargs):
        pass