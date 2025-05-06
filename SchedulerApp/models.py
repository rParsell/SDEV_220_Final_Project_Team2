from django.conf import settings
from django.db import models


class RawData(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Emplpoyee in question( Employee1 - Employee50)
    shift = models.CharField(max_length=20) #Shift worked: 1st, 2nd, ord 3rd
    department = models.CharField(max_length=20) #Department worked in(Grocery, Meat, or Customer Service)
    hours = models.CharField(max_length=20) #hours worked per week
    dayOff = models.CharField(max_length=20) #Day off
    ptoft = models.CharField(max_length=2) #Part Time or Full Time (PT or FT)
    Sunday = models.CharField(max_length=20)
    Monday = models.CharField(max_length=20)
    Tuesday = models.CharField(max_length=20)
    Wednesday = models.CharField(max_length=20)
    Thursday = models.CharField(max_length=20)
    Friday = models.CharField(max_length=20)
    Saturday = models.CharField(max_length=20)

    def __str__(self):
        return self.employee
# Create your models here.
