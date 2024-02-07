from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils import timezone
import random
import string
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=500,unique=True, null=True,blank=True)
    address =models.CharField(max_length=1000,unique=True, null=True,blank=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=150, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=150,null=True, blank=True)
    department =models.ForeignKey(Department,on_delete=models.SET_NULL,null=True, blank=True)
    exam = models.BooleanField(default=True,null=True, blank=True)
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        if not self.id and not self.password:
            self.set_password(self.last_name.lower())

        super().save(*args, **kwargs)

    objects=UserManager( )
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['first_name','last_name']

    class Meta:
        ordering = ['-department']
        indexes = [
            models.Index(fields=['-department']),
        ]
    
    def __str__(self):
        return f"{self.email}"