# -*- coding: utf-8 -*-
import re

from django.http.request import HttpRequest
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage
from pydantic import BaseModel, EmailStr, field_validator

from apps.main import models
from vinat.settings import EMAIL_HOST_USER, DEBUG

class ProductPOSTRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None
    name: str | None = None
    product_id: str | None = None

    @field_validator('phone')
    def check_age(cls, value):
        PHONE_REGEX = re.compile(r'[(+7)8]\(?\d{3}\)?\d{3}[\-\w]?\d{2}[\-\w]?\d{2}')
        matched = PHONE_REGEX.match(value)
        if not matched:
            raise ValueError('invalid phone')
        return value


class ProductView(View):
    """Base class for product handlers"""
    
    page = 'main.html'
    product_name = 'нефтепродукт'

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.page)

    def post(self, request: HttpRequest, *args, **kwargs):
        keys = ['email', 'phone', 'product_id', 'name']
        #request.is_secure()
        request_data = ProductPOSTRequest(**request.POST)
        self.send_demand(request_data)

        return self.get(request)

    def send_demand(self, request: ProductPOSTRequest):
        if request.email == None or request.email == '':
            request.email = 'не указан'
        if request.phone == None or request.phone == '':
            request.phone = 'не указан'
        text = ('Пользователь представившийся как \'{0}\' оставил заявку на покупку {4} марки {1}.' + 
        '\n Его контакты:\n\tТелефон: {2}\n\temail: {3}').format(request.name, request.product_id, request.phone, request.email, self.product_name)
        com = models.Company()
        mail = EmailMessage('Заявка на покупку {0} марки {1}'.format(self.product_name, request.product_id), text, EMAIL_HOST_USER, com.email())
        if DEBUG:
            print(mail)
        else:
            mail.send()
