from django.db import models
from accounts.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/tasks")
    requiredSize = models.IntegerField(default=10000)
