from django.db import models
from django.urls import reverse
from registration.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.

# fs = FileSystemStorage(location='/media/photos')

class Event(models.Model):
    organiser = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.IntegerField()
    image = models.ImageField(storage='static/images')
    visible = models.BooleanField(default=True)

    def get_absolute_url(self):
         return reverse("events:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
