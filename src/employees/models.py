from django.db import models

class Beneficiary(models.Model):
    Name = models.CharField(max_length=255)
    Relationship = models.CharField(max_length=255)
    BirthDate = models.DateTimeField()
    Gender = models.CharField(max_length=255)
    IsDeleted = models.BooleanField(default=False)

class Employee(models.Model):
    Photo = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    JobPosition = models.CharField(max_length=255)
    Wage = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=255)
    HireDate = models.DateTimeField()
    IsDeleted = models.BooleanField(default=False)
    Beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='employee')

