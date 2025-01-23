from django.db import models

# Create your models here.

class MovieDB(models.Model):
    title = models.TextField(max_length=100) 
    year = models.IntegerField(null=True)


class MovieHitchart(models.Model):
    Budget = models.IntegerField(null=True)
    BoxOffice = models.IntegerField(null=True)
    
