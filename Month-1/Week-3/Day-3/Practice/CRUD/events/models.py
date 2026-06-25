from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField()
    guest = models.IntegerField()

    def _str_(self):
        return self.name