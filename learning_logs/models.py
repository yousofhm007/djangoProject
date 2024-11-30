from django.db import models

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
