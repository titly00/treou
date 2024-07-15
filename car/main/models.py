from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=232)
    text_problem = models.TextField()
    date_problem = models.DateField()
    contact_info = models.CharField(max_length=232)

    def __str__(self):
         return self.name
