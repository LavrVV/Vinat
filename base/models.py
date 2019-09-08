# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import os

import json
from vinat.settings import BASE_DIR

# Create your models here.
class Product(models.Model):
    passport = models.FilePathField()
    name = models.TextField()

class PVD(Product):
    pass

class PS(Product):
    pass

class PP(Product):
    pass

class Partner(models.Model):
    name = models.TextField()
    logo = models.FilePathField()
    link = models.URLField()

class Company:
    '''singleton uses to represent company contacts as json object'''
    def __init__(self):
        dir = BASE_DIR
        module_dir = os.path.dirname(__file__)
        with open(os.path.join(module_dir, 'data/company.json'), 'r') as com_file:
            data = json.load(com_file)
        self._phone = data['phone']
        self._email = data['email']
        self._adress = data['adress']

    def phone(self, phone=None, save=True):
        if phone != None:
            self._phone = phone
            if save:
                self.save()
        return self._phone
    def email(self, email=None, save=True):
        if email != None:
            self._email = email
            if save:
                self.save()
        return self._email

    def adress(self, adress=None, save=True):
        if adress != None:
            self._adress = adress
            if save:
                self.save()
        return self._adress
    
    def save(self):
        data = {
            'phone' : self._phone,
            'email' : self._email,
            'adress' : self._adress
        }
        module_dir = os.path.dirname(__file__)
        with open(os.path.join(module_dir, 'data/company.json'), 'w') as com_file:
            json.dump(data, com_file)
        
        #json.dump(data, '/data/company.json')
