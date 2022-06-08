from django.db import models

# Create your models here.


class EyeColour(models.Model):
    EYE_COLOUR_CHOICES = [
        ('BLU', 'Blue'),
        ('GR', 'Green'),
        ('BRW', 'Brown'),
        ('HZ', 'Hazel')
    ]
    eyeColour = models.CharField(
        max_length=5, choices=EYE_COLOUR_CHOICES, default='Any')
