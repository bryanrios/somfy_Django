from django.db import models

class Controller(models.Model):
    name = models.CharField(max_length=20)
    display = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    sort = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
