# -*- coding: utf-8 -*-
import os
import json

from django.db import models

class Product(models.Model):
    passport = models.FileField(upload_to='passports')
    name = models.TextField()

    def __str__(self):
        return self.name

class PVD(Product):
    pass

class PS(Product):
    pass

class PP(Product):
    pass

class Partner(models.Model):
    name = models.TextField()
    logo = models.FileField(upload_to='logos')
    link = models.URLField()
    
    def __str__(self):
        return self.name

class Company:
    '''singleton uses to represent company contacts as json object'''
    def __init__(self):
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
