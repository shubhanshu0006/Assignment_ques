from django.db import models
class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    author = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
# Create your models here.
