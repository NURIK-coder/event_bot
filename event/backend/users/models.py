from django.contrib.auth.models import AbstractUser
from django.db import models




# Create your models here.





class TGUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    role = models.CharField('Role', max_length=10, default='user')
    events = models.ManyToManyField('events.Event', blank=True)

    def __str__(self):
        return self.role


