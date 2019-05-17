from django.db import models

# Create your models here.
class Rating(models.Model):
    rating = models.IntegerField(default=0)
    def publish(self):
        self.save()
