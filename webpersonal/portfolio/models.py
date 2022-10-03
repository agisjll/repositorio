from email.mime import image
from turtle import update
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Project (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    



