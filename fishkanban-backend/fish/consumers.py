from datetime import datetime
from random import randint

# from channels import Group
# from channels.sessions import channel_session
# from channels.auth import channel_session_user
from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

from fish.models import Fish

import logging

logger = logging.getLogger(__name__)

class FishEventConsumer(JsonWebsocketConsumer):
    groups = ["notifications"]

    # @channel_session_user
    def connect(self):
        # Called on connection.
        logger.info('websocket_connect. message = %s', self)
        async_to_sync(self.channel_layer.group_add)("notifications", self.channel_name)
        # Group("notifications").add(self.reply_channel)
        self.accept()
        # Or to reject the connection, call
        # self.close()
        # transfer_user(message.http_session, message.channel_session)

    def receive_json(self, content):
        # Called with either text_data or bytes_data for each frame
        logger.info(content)
        action = content.get("action", None)
        if action == 'test':
            fishId = randint(0,1000000000)
            testFish = Fish(fishId=fishId, fishDateTime=datetime.now(), fishType=Fish.FISH_TYPE_TUNA, fishState=Fish.FISH_STATE_NEW, fishDetails="Blah" )
            testFish.save()
        elif command == 'save':
            testFish = Fish(content[fish])
        elif action == 'log':
            logger.info("Got the Signal!!")

        # You can call:
        # self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Calls:
        # self.close()
        # Or add a custom WebSocket error code!
        # self.close(code=4123)


    def fish_create(self, event):
        logger.info("New Fish!!!")
        self.send(text_data=event["data"])

    # @channel_session
    def disconnect(self, close_code):
        # Called when the socket closes
        logger.info('websocket_disconnect. message = %s', self)
        async_to_sync(self.channel_layer.group_discard)("notifications", self.channel_name)
        # Group("notifications").discard(self.reply_channel)
