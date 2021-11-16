from django.db import models

"""
Model wich represent a company (p. ex. Amazon, E-commerce and cloud computing services ).
"""
class Company(models.Model):
    code = models.CharField(max_length=18, unique=True)
    name = models.TextField(max_length=200)
    active = models.BooleanField(auto_now_add=True)

    def __str__(self):
            return self.name