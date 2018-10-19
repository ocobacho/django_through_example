from django.db import models

# Create your models here.
class CompanyGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    groups = models.ManyToManyField(CompanyGroup, related_name='groups', blank=True)