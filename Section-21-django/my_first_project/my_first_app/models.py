from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(verbose_name="First name", max_length=30)
    last_name = models.CharField(verbose_name="Last name", max_length=30)
