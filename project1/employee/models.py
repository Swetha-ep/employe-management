from django.db import models

# Create your models here.

class Employees(models.Model):
    DEP_CHOICES = [
        ('IT','Information Technology'),
        ('HR','Human Resources'),
        ('Finance','Finance'),
    ]
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    department= models.CharField(max_length=30,choices=DEP_CHOICES)

    def __str__(self):
        return self.name