from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullName = models.CharField(max_length=128)
    webside = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    
    def _str_(self):
        return self.fullName + '('+ self.username +')'

