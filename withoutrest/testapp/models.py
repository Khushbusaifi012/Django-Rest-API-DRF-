from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)

class College(models.Model):
    cname=models.CharField(max_length=100)
    ccourse=models.CharField(max_length=100)
    csubjects=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)