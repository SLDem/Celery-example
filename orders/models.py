from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    employee = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
