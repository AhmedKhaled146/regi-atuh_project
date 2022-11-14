from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile')
    job = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    about = models.TextField(max_length=1500)
    year_of_experinse = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return str(self.user)

####
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
