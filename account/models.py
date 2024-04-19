from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12 , blank=True , null=True)
    birth_date = models.DateField(blank=True , null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'