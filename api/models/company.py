from django.db import models

"""
Model wich represent a company (p. ex. unique_code_from_amazon, Amazon, true ).
"""
class Company(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.TextField(max_length=200)
    active = models.BooleanField(default=True)