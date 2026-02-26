from django.db import models


# Create your models here.
class ClientModel(models.Model):
    name = models.CharField(max_length=500)
    mail = models.EmailField(max_length=500)
    phone = models.PositiveBigIntegerField()
    date = models.DateField()
    password = models.CharField(max_length=500)
    objects = models.Manager()


class ClientRegFreelance(models.Model):
    name = models.CharField(max_length=500)
    mail = models.EmailField(max_length=500)
    mobile = models.PositiveBigIntegerField()
    category = models.CharField(max_length=500)
    industry = models.CharField(max_length=500)
    business_scale = models.CharField(max_length=500)
    user_type = models.CharField(max_length=500)
    no_of_users = models.CharField(max_length=500)
    deployment = models.CharField(max_length=500)
    os = models.CharField(max_length=500)
    mobile_app = models.CharField(max_length=500)
    # emp_mail = models.EmailField(max_length=500, null=True)
    pricing = models.CharField(max_length=500, null=True)
    approve = models.BooleanField(default=False)
    client_approve = models.BooleanField(default=False)
    to_employee = models.BooleanField(default=False)
    accept_project = models.BooleanField(default=False)
    finish_project = models.BooleanField(default=False)
    send_pricing = models.BooleanField(default=False)
    objects = models.Manager()


class ClientRegInhouse(models.Model):
    name = models.CharField(max_length=500)
    mail = models.EmailField(max_length=500)
    mobile = models.PositiveBigIntegerField()
    category = models.CharField(max_length=500)
    industry = models.CharField(max_length=500)
    business_scale = models.CharField(max_length=500)
    user_type = models.CharField(max_length=500)
    no_of_users = models.CharField(max_length=500)
    deployment = models.CharField(max_length=500)
    os = models.CharField(max_length=500)
    mobile_app = models.CharField(max_length=500)
    pricing = models.CharField(max_length=500, null=True)
    approve = models.BooleanField(default=False)
    client_approve = models.BooleanField(default=False)
    accept_project = models.BooleanField(default=False)
    finish_project = models.BooleanField(default=False)
    send_pricing = models.BooleanField(default=False)
    objects = models.Manager()
