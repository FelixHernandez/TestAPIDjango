from django.db import models

class Employee(models.Model):
    Photo = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    JobPosition = models.CharField(max_length=255)
    Wage = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=255)
    HireDate = models.DateTimeField()
    IsDeleted = models.BooleanField(default=False)

class Beneficiary(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='beneficiaries')
    Name = models.CharField(max_length=255)
    Relationship = models.CharField(max_length=255)
    BirthDate = models.DateTimeField()
    Gender = models.CharField(max_length=255)
    IsDeleted = models.BooleanField(default=False)
