from django.db import models

class Employee(models.Model):
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    job_position = models.CharField(max_length=255)
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    hire_date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

class Beneficiary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='beneficiaries')
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
