from django.db import models
import datetime

# Create your models here.
class Cancer(models.Model):
    type_of_cancer = models.CharField(max_length=35)
    description = models.CharField(max_length=3000)
    symptoms = models.CharField(max_length=5000)
    treatment = models.CharField(max_length=5000)

    def __str__(self):
        return self.type_of_cancer
    

class Post(models.Model):
    msg_description = models.CharField(max_length=5000)
    period = models.IntegerField()
    date = models.DateTimeField(default= datetime.datetime.today)

    def __str__(self):
        return self.msg_description




