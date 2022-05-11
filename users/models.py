from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Child(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

class Tag(models.Model):
    title = models.CharField(max_length=255)

class Parent(models.Model): 
    title = models.CharField(max_length=255, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

