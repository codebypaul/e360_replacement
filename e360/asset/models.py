from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.TextField(blank=True,null=True)
    active_jobsite=models.BooleanField(default=False)

    def __str__(self):
        return self.location_name
    
    class Meta:
        ordering = ['location_name']