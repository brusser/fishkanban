from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from fish.consumers import FishEventConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    # WebSocket fish status event handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("event", FishEventConsumer)
        ])
    ),

})
