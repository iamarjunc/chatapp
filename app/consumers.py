import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync


class MychatApp(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("connecting...........")
        await self.accept()
        
        
    async def receive(self,text_data):
        pass
    
    async def disconnect(self):
        pass