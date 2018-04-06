from fish.models import Fish

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# from channels import Group

from json import dumps

import logging

logger = logging.getLogger(__name__)


def send_notification(notification):
    logger.info('send_notification. notification = %s', notification)
    # logger.info('send_notification. notification json = %s', dumps(notification))
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notifications", { 'type' : notification['type'], 'data' : notification['data'],})

@receiver(post_save, sender=Fish)
def fish_post_save(sender, instance, created, **kwargs):
    send_notification({
        'type': 'fish.create',
        'created': created,
        'data': instance.fishProtoJson
    })

@receiver(post_delete, sender=Fish)
def fish_post_delete(sender, instance, created, **kwargs):
    send_notification({
        'type': 'fish.delete',
        'data': instance.fishProtoJson
    })