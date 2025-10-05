from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    descripton = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_created=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
     
    def __str__(self):
        return self.title