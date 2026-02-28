from django.db import models
from django.utils import timezone

class Student(models.Model):
    roll_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, unique=True)
    village = models.CharField(max_length=50, default='Karola')
    admission_date = models.DateField(default=timezone.now)


    def __str__(self):
        return f"{self.roll_no} - {self.name}"