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
    product_name = 'нефтепродукт'

    def get(self, request, *args, **kwargs):
        return render(request, self.page)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        phone = request.POST.get('phone number')
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        #request.POST.
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
        summary = 'Компания предлагает купить гранулы полистирола оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
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
        summary = 'Компания предлагает купить гранулы полистирола оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {'products': models.PP.objects.all(),
                'summary' : summary,
                'header' : 'Полипропилен',
                'title' : 'PP'
            }
        return render(request, self.page, context=data)
