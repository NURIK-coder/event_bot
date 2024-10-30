from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField('Title', max_length=200)
    date = models.DateField('Date')
    location = models.CharField('Location', max_length=100)
    description = models.TextField('Description')
    created_at = models.DateTimeField('Created_at', auto_now_add=True)

    def __str__(self):
        return self.title
