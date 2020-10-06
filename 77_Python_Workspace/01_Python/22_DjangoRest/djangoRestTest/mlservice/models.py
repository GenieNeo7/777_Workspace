from django.db import models

# Create your models here.
class Request(models.Model):
    requestedDate = models.DateTimeField(auto_now=True)
    orderNumber = models.CharField(max_length=200)