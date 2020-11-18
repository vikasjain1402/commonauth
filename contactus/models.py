from django.db import models

# Create your models here.

class Contactusmodel(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.ImageField(blank=False)
    subject=models.CharField(max_length=100,blank=False)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name+":"+self.subject

