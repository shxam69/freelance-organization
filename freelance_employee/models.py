from django.db import models


# Create your models here.
class FreelanceEmployeeModel(models.Model):
    name = models.CharField(max_length=500)
    mail = models.EmailField(max_length=500)
    phone = models.PositiveBigIntegerField()
    date = models.DateField()
    password = models.CharField(max_length=500)
    objects = models.Manager()


class FreelanceEmployee(models.Model):
    name = models.CharField(max_length=500)
    emp_id = models.CharField(max_length=500)
    mail = models.EmailField(max_length=500)
    gender = models.CharField(max_length=500)
    age = models.IntegerField()
    education = models.CharField(max_length=500)
    job_title = models.CharField(max_length=500)
    salary = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    experience = models.IntegerField()
    approve = models.BooleanField(default=False)
    client_approve = models.BooleanField(default=False)
    from_client = models.BooleanField(default=False)
    objects = models.Manager()
