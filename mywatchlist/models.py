from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()
