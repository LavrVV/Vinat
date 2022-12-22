# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from base import models
from vinat.settings import DEFAULT_FROM_EMAIL

import re

class MainView(View):
    """Main page handler (/)"""
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')

    def post(self, request, *args, **kwargs):
        pass

class ProductView(View):
    """Base class for product handlers"""
    
    page = 'main.html'
    product_name = 'нефтепродукт'

    def get(self, request, *args, **kwargs):
        return render(request, self.page)

    def post(self, request, *args, **kwargs):
        keys = ['email', 'phone number', 'product_id', 'name']
        #request.is_secure()
        for key, value in request.POST.items():
            if key in keys:
                if key == keys[0]:
                    email = value
                    EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+(?:\.[^@\s]+)+")
                    if not EMAIL_REGEX.match(email):
                        print(email)
                        #wrong email
                elif key == keys[1]:
                    phone = value
                    if len(phone) == 12 and phone[0] == '+':
                        if not phone[1:].isdigit():
                            print(phone)
                            #wrong phone
                    elif len(phone) == 11:
                        if not phone.isdigit():
                            print(phone)
                            #wrong phone
                    else:
                        print(phone)
                        #wrong phone
                elif key == keys[2]:
                    product_id = value
                elif key == keys[3]:
                    name = value
            else:
                #some unexpexted key
                print(key)
                return self.get(request)
        self.send_demand(name, email, phone, product_id)

        return self.get(request)

    def send_demand(self, name, demander_email, demander_phone, product_id):
        if demander_email == None or demander_email == '':
            demander_email = 'не указан'
        if demander_phone == None or demander_phone == '':
            demander_phone = 'не указан'
        text = ('Пользователь представившийся как \'{0}\' оставил заявку на покупку {4} марки {1}.' + 
        '\n Его контакты:\n\tТелефон: {2}\n\temail: {3}').format(name, product_id, demander_phone, demander_email, self.product_name)
        com = models.Company()
        mail = EmailMessage('Заявка на покупку {0} марки {1}'.format(self.product_name, product_id), text, DEFAULT_FROM_EMAIL, com.email())
        #mail.send()
    
class PSView(ProductView):
    """Polystyrene page handler (/ps)"""
    
    page = 'product.html'
    product_name = 'полистерола'

    def get(self, request, *args, **kwargs):
        summary = 'Компания предлагает купить гранулы полистирола оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {'products': models.PS.objects.all(),
                'summary' : summary,
                'header' : 'Полистерол',
                'title' : 'PS'
            }
        return render(request, self.page, context=data)

        

class PVDView(ProductView):

    page = 'product.html'
    product_name = 'ПВД'

    """PVD page handler (/pvd)"""
    def get(self, request, *args, **kwargs):
        summary = 'Компания предлагает купить гранулы ПВД оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {'products': models.PVD.objects.all(),
                'summary' : summary,
                'header' : 'ПВД',
                'title' : 'PVD'
            }
        return render(request, self.page, context=data)


class PPView(ProductView):

    page = 'product.html'
    product_name = 'полипропилена'

    """polypropylene page handler (/pp)"""
    def get(self, request, *args, **kwargs):
        summary = 'Компания предлагает купить гранулы полипропилена оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {'products': models.PP.objects.all(),
                'summary' : summary,
                'header' : 'Полипропилен',
                'title' : 'PP'
            }
        return render(request, self.page, context=data)
