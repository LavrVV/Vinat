# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from base import models
from vinat.settings import DEFAULT_FROM_EMAIL

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
        data = {'products': models.PS.objects.all()}
        return render(request, self.page, context=data)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        phone = request.POST.get('phone number')
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        
        #self.send_demand(name, email, phone, product_id)

        return render(request, self.page)

    def send_demand(self, name, demander_email, demander_phone, product_id):
        if demander_email == None or demander_email == '':
            demander_email = 'не указан'
        if demander_phone == None or demander_phone == '':
            demander_phone = 'не указан'
        text = ('Пользователь представившийся как \'{0}\' оставил заявку на покупку полистерола марки {1}.' + 
        '/n Его контакты:/n/tТелефон: {2}/n/temail: {3}').format(name, product_id, demander_phone, demander_email)
        com = models.Company()
        mail = EmailMessage('Заявка на покупку полистерола марки {0}'.format(product_id), text, DEFAULT_FROM_EMAIL, com.email())
        #mail.send()
        

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