from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from fish.consumers import FishNotificationsConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    # WebSocket fish status notifications handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("notifications", FishNotificationsConsumer)
        ])
    ),
    # "websocket": URLRouter([
    #     path("notifications/", FishNotificationsConsumer)
    # ])
})
