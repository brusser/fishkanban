from django.db import models


# Create your models here.

class Fish(models.Model):

    FISH_TYPE_SALMON = 'SALMON'
    FISH_TYPE_TUNA = 'TUNA'
    FISH_TYPE_CHOICES = (
        (FISH_TYPE_SALMON, 'Salmon'),
        (FISH_TYPE_TUNA, 'Tuna'),
    )
    FISH_STATE_NEW = 'NEW'
    FISH_STATE_PROCESSING = 'PROCESSING'
    FISH_STATE_COMPLETED = 'COMPLETED'

    FISH_STATE_CHOICES = (
        (FISH_STATE_NEW, 'New'),
        (FISH_STATE_PROCESSING, 'Processing'),
        (FISH_STATE_COMPLETED, 'Completed'),
    )

    fishId = models.IntegerField(primary_key=True)
    fishDateTime = models.DateTimeField()
    fishType = models.CharField(choices=FISH_TYPE_CHOICES, max_length=256)
    fishTags = models.TextField(blank=True)
    fishDetails = models.TextField(blank=True)
    fishState = models.CharField(max_length=256, choices=FISH_STATE_CHOICES, default=FISH_STATE_NEW)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
