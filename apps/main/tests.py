# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.main.views.product import ProductPOSTRequest

# Create your tests here.
class TestValidation(TestCase):
    def test_product_id(self):
        input = {
            'product_id': 'pvd'
        }
        result = ProductPOSTRequest(**input)
        assert result.product_id == 'pvd'
