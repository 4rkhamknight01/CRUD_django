from django.db import models

# Create your models here.

class position(models.Model):
    title = models.CharField(max_length=20)

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    mobile_no = models.CharField(max_length=10)
    position = models.ForeignKey(position, on_delete=models.CASCADE)