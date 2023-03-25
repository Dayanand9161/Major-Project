from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    pass

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YoutTube','Youtube'),
        ('Google','Google'),
        ('Newsletter','newsletter'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)

    # phoned = models.BooleanField(default = False)
    # source = models.CharField(choices=SOURCE_CHOICES,max_length=100)
    # profile_picture = models.ImageField(blank=True,null = True)
    # special_files = models.FileField()
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user.email


    
    


