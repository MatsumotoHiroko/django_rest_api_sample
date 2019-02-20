from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    context = models.CharField(max_length=1024, blank=False, null=False)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    category = models.OneToOneField('Categories', models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Categories(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)