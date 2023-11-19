from django.db import models
from instructor.models import Instructor

from datetime import datetime

class Course(models.Model):

    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)

    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')

    is_published = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

