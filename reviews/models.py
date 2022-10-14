from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    movie_name = models.TextField()
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

