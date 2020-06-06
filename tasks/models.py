from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=58, blank=False)
    description = models.TextField(max_length=200, blank=True, default='')
    priority = models.IntegerField(default=3)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id) + ' | ' + self.title