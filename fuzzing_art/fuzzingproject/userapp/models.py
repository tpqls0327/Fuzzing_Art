from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class AccountUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=20)     # 이름
    nickname = models.CharField(max_length=20)     # 별명
    gender = models.IntegerField()   # 0:여자 1:남자
    age = models.IntegerField()    # 나이
    address = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name