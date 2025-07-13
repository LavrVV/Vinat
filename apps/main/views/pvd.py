# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http.request import HttpRequest
from apps.main.views.product import ProductView
from apps.main import models

class PVDView(ProductView):

    page = 'product.html'
    product_name = 'ПВД'

    """PVD page handler (/pvd)"""
    def get(self, request: HttpRequest, *args, **kwargs):
        summary = 'Компания предлагает купить гранулы ПВД оптом и в розницу от ведущих российских производителей. Мы гарантируем высокое качество продукции, соответствующее современным стандартам и нормам, а также выгодные условия поставок и индивидуальные условия обслуживания.'
        data = {
            'products': models.PVD.objects.all(),
            'summary' : summary,
            'header' : 'ПВД',
            'title' : 'PVD'
        }
        return render(request, self.page, context=data)
