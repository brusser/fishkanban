from django.db import models

from json import dumps

import fish.fish_pb2 as fish_pb2
from google.protobuf.json_format import MessageToJson

import logging

logger = logging.getLogger(__name__)

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



    @property
    def fishProtoJson(self):
        proto = fish_pb2.Fish()
        
        proto.id = self.fishId
        proto.date_time = str(self.fishDateTime)
        if self.fishType == Fish.FISH_TYPE_SALMON :
            proto.type = fish_pb2.Fish.SALMON
        elif self.fishType == Fish.FISH_TYPE_TUNA :
            proto.type = fish_pb2.Fish.TUNA

        if self.fishState == Fish.FISH_STATE_NEW :
            proto.state = fish_pb2.Fish.NEW
        elif self.fishState == Fish.FISH_STATE_PROCESSING :
            proto.state = fish_pb2.Fish.PROCESSING
        elif self.fishState == Fish.FISH_STATE_COMPLETED :
            proto.state = fish_pb2.Fish.COMPLETED

        proto.tags = self.fishTags
        proto.details = self.fishDetails

        logger.debug("Model Protobuf Message: %s", MessageToJson(fishP))
        return MessageToJson(proto)





