from django.db import models

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Entry(models.Model):
    topic_id = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name_plural = 'entries'

            def __str__(self):
                return f"{self.text[:50]}..."


