from django.db import models
from django.utils import timezone

class ContactSender(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.TextField(max_length=255)
    message = models.TextField(max_length=500)
    email = models.EmailField(max_length=254, null=False, blank=False, default="")
    marked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Donation(models.Model):
    donor_name = models.CharField(max_length=50, default="", blank=False)
    amount = models.IntegerField(default=100)
    date = models.DateTimeField(default=timezone.now())
    message = models.TextField(max_length=1000, default="", blank=True)
    #certificate = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

# Create your models here.
