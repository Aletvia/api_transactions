from django.db import models

from api.models.company import Company

"""
Model wich represent a Transaction (p. ex. 20, E-commerce and cloud computing services ).
"""
class Transaction(models.Model):
    STATUS = (
        ('c', 'Closed'),
        ('r', 'Reversed'),
        ('P', 'Pending'),
        ('f', 'Funding-user'),
    )
    folio = models.CharField(max_length=20, default='-')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.CharField(max_length=11, default=0)
    date = models.DateTimeField(null=False)
    transaction_status = models.CharField(max_length=1, choices=STATUS)
    charged = models.BooleanField(default=False)