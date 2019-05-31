from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    DESIG_CHOICES = (
        ('Organiser', 'Organiser'),
        ('Attendee', 'Attendee'),
    )
    desig = models.CharField(max_length=20, choices=DESIG_CHOICES)

    def get_absolute_url(self):
         return reverse("tcapp:detailview",kwargs={'pk':self.pk})
