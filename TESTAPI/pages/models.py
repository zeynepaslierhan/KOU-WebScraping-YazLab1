from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# python manage.py makemigrations appismi      -> ile migration oluşturulur.
# python manage.py migrate pages               -> ile migration database'e yansıtılır.

class Todo(models.Model):
    task=models.CharField(max_length=30)
    description=models.CharField(max_length=100)

class Departments(models.Model):
    DepartmendId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
 