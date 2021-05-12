from django.db import models
from django.utils import timezone


# Create your models here.


class ResponseLog(models.Model):
    ResponseTime = models.DurationField()
    Url = models.CharField(max_length=255)
    Name = models.CharField(max_length=50)
    ResponseCode = models.CharField(max_length=3)
    queried_at = models.DateTimeField(auto_now_add=True)
