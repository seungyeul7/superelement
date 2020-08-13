from django.db import models

# Create your models here.
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(default='', null=True, blank=True, max_length=255)
    gender = models.CharField(default='', null=True, blank=True, max_length=16)
    birthday = models.DateField()
