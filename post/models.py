from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=280)
    roast_or_boast = models.BooleanField()
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    time_created = models.DateTimeField(default=timezone.now)
    @property
    def votetotal(self):
        return self.up_vote + self.down_vote

