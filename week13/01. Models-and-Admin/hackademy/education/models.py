from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    lecture_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    week = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)

    def __str__(self):
        return f'Lecture "{self.name}"'


class Task(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Task "{self.name}"'

