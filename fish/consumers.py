import json
from datetime import datetime
import logging
from random import randint

from channels.generic.websocket import WebsocketConsumer
from fish.models import Fish

class FishNotificationsConsumer(WebsocketConsumer):
    groups = ["notifications"]

    def connect(self):
        # Called on connection. Either call
        self.accept()
        # Or to reject the connection, call
        # self.close()

    def receive(self, text_data=None):
        logger = logging.getLogger('WS_Receive')
        # Called with either text_data or bytes_data for each frame
        logger.error(text_data)
        data = json.loads(text_data)
        logger.error(data)
        action = data['action']
        logger.error(action)
        if action == 'test':
            fishId = randint(0,1000000000)
            testFish = Fish(fishId=fishId, fishDateTime=datetime.now(), fishType=Fish.FISH_TYPE_SALMON, fishState=Fish.FISH_STATE_NEW )
            testFish.save()

        # You can call:
        # self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        # self.close()
        # Or add a custom WebSocket error code!
        # self.close(code=4123)

    def disconnect(self, close_code):
        # Called when the socket closes
        pass
