from django.db import models


class Customer(models.Model):

    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    ContactNumber = models.IntegerField
    Address = models.CharField(max_length=255)
    PetName = models.CharField(max_length=255)
    Breed = models.CharField(max_length=255)
