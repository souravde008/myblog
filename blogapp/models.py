from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=100)
    user_mail = models.EmailField(max_length=70)
    user_phone = models.CharField(max_length=100)
    user_password = models.CharField(max_length=200,default='ABCD')
