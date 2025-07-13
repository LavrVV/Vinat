# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http.request import HttpRequest
from apps.main.views.product import ProductView
from apps.main import models

class PPView(ProductView):

    page = 'product.html'
    product_name = 'полипропилена'

    """polypropylene page handler (/pp)"""
    def get(self, request: HttpRequest, *args, **kwargs):
        summary = 'Компания предлагает купить гранулы полипропилена оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {
            'products': models.PP.objects.all(),
            'summary' : summary,
            'header' : 'Полипропилен',
            'title' : 'PP'
        }
        return render(request, self.page, context=data)
