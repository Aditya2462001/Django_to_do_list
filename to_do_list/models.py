from django.db import models

# Create your models here.

class Data(models.Model):
    content = models.CharField(max_length=500)
    time_field = models.TimeField(auto_now=True)
    date_field = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
    