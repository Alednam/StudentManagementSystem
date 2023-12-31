from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from datetime import datetime

class Instructor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='instructors/photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=70)
    registered_date = models.DateTimeField(default=datetime.now, blank=True)
    is_mvp = models.BooleanField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
