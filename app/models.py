from django.db import models

# Create your models here.


class Student(models.Model):
    SID=models.IntegerField(primary_key=True)
    SNAME=models.CharField(max_length=100)
    SMAIL=models.EmailField(max_length=50)
    SMARKS=models.IntegerField()
    SAGE=models.IntegerField()



class Employee(models.Model):
    EID=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=50)
    ESAL=models.IntegerField()