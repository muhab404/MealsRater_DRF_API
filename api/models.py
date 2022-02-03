from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=320)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    
    def avg_rating(self):
        # sum of ratings stars  / len of rating hopw many ratings 
        sum = 0
        ratings = Rating.objects.filter(meal=self) # no of ratings happened to the meal 

        for x in ratings:
            sum += x.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.meal.title

    class Meta:

        # to ensure the user will rate just once
        unique_together=(('user','meal'),)    
        index_together=(('user','meal'),)    
