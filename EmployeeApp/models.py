from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentsId = models.AutoField(primary_key=True)
    DepartmentsName = models.CharField(max_length=550)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=550)
    Departments = models.CharField(max_length=550)
    DateOfJoining = models.DateField()
    PhotoFileNAme = models.CharField(max_length=550)