# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http.request import HttpRequest
from apps.main.views.product import ProductView
from apps.main import models

class PSView(ProductView):
    """Polystyrene page handler (/ps)"""
    
    page = 'product.html'
    product_name = 'полистерола'

    def get(self, request: HttpRequest, *args, **kwargs):
        summary = 'Компания предлагает купить гранулы полистирола оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {
            'products': models.PS.objects.all(),
            'summary' : summary,
            'header' : 'Полистерол',
            'title' : 'PS'
        }
        return render(request, self.page, context=data)
