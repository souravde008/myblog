from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=100)
    user_mail = models.EmailField(max_length=70,unique=True)
    user_phone = models.CharField(max_length=100)
    user_password = models.CharField(max_length=200,default='ABCD')


class Blogs(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE,default=None)
	blog_title=models.CharField(max_length=255, default='Title Unavailable')
	blog_desc = models.CharField(max_length=255, default='Description Unavailable')
	blog_created_at = models.DateField()
	blog_img = models.FileField(upload_to="blog/",default="")

	