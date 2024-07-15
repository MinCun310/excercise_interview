from django.db import models


# Create your models here.

class Staff(models.Model):
    staff_id = models.CharField(unique=True,max_length=20)
    japanese_name = models.CharField(max_length=60)
    english_name = models.CharField(max_length=50)
    category = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
