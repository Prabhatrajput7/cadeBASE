from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

from .models import *

##################### BASIC

# class MyC(SyncConsumer):

#     def websocket_connect(self,event):
#         print('inside connect', event)
#         self.send({
#             'type':'websocket.accept'
#         })

# this should be like this no custom key value self.send({'type':'websocket.accept'})        
    # def websocket_receive(self,event):
    #     print('inside recieve', event)
    #     for i in range(10):
    #         self.send({
    #             'type':'websocket.send',
    #             'text': str(i)
    #         })
    #         sleep(1)

#     def websocket_receive(self,event):
#         print('inside recieve', event)
#         for i in range(10):
#             self.send({
#                 'type':'websocket.send',
#                 'text': json.dumps({'count':i})
#             })
#             sleep(1)

#     def websocket_disconnect(self,event):
#         print('inside disconnect', event)
#         raise StopConsumer()

# class AMyC(AsyncConsumer):

#     async def websocket_connect(self,event):
#         print('inside aconnect', event)
#         await self.send({
#             'type':'websocket.accept'
#         })

#     async def websocket_receive(self,event):
#         print('inside arecieve', event)
#         for i in range(10):
#             await self.send({
#                 'type':'websocket.send',
#                 'text': str(i)
#             })
#             await asyncio.sleep(1)

#     async def websocket_disconnect(self,event):
#         print('inside adisconnect', event)
#         raise StopConsumer()





#########################################################################################################################


################# CHAT


# Note when js make connection first it will run websocket_connect
# when js sent it will revieve

from asgiref.sync import async_to_sync
# group fx is async by default so using  async_to_sync

class ChatappSync(SyncConsumer):

    def websocket_connect(self,event):
        print('inside connect', event)
        # get default channel layer RedisChannelLayer(hosts=[{'address': ('localhost', 6379)}])
        # print(self.channel_layer)
        # get defult channel name specific.de6c4e20fdd44ba9a0e9c04257c3ae0f!4444b435f3bb47789340b71dfc06e7d1
        # when we open the wc url in 2 tab it will generate 2 channel layer and we need to connect them using grp
        # print(self.channel_name)

        #  adding channel name to grp siege when you open ws url any new channel name will go in this grp
        async_to_sync(self.channel_layer.group_add)('siege',self.channel_name)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('inside recieve', event)

        async_to_sync(self.channel_layer.group_send)('siege',{
            'type':'chat.message',
            'message':event['text']
        })


    def chat_message(self,event):
        # 'message':event['text'] this is event in this 
        print('chat event',event)
        self.send({
            'type':'websocket.send',
            'text': event['message']
        })


        # the below code will not work qwith grps
        # self.send({
        #         'type':'websocket.send',
        #         'text': event['text']
        #     })


    def websocket_disconnect(self,event):
        print('inside disconnect', event)
        async_to_sync(self.channel_layer.group_discard)('siege',self.channel_name)
        raise StopConsumer()


from channels.db import database_sync_to_async
#  making the above code async

class ChatappASync(AsyncConsumer):

    async def websocket_connect(self,event):
        print('inside connect', event)
        self.gp = self.scope['url_route']['kwargs']['gpn']
        await self.channel_layer.group_add(self.gp,self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('inside recieve', event)

        user = self.scope['user']
        if user.is_authenticated:

            g = await database_sync_to_async(Group.objects.get)(name = self.gp)
            d = json.loads(event['text'])
            d['username'] = user.username
            # orm is sync by default
            await database_sync_to_async(Chat.objects.create)(content= d['mg'],grp=g)

            await self.channel_layer.group_send(self.gp,{
                'type':'chat.message',
                # 'message':event['text']
                'message':json.dumps(d)
            })
        
        else:
            await self.send({
            'type':'websocket.send',
            'text': json.dumps({'mg':'Login Required','username':'Unknow'})
        })

    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self,event):
        print('inside disconnect', event)
        await self.channel_layer.group_discard(self.gp,self.channel_name)
        raise StopConsumer()



#########################################################################################################################

###################### BASIC 2

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class MySync(WebsocketConsumer):

    def connect(self):
        print('connected')
        self.accept()
        # self.close() to accept and close inmmediatalty

    def receive(self, text_data=None, bytes_data=None):
        print('recieve', text_data)
        #  text data messge from client  
        self.send(text_data='Message from DJ')      
        # self.send(bytes_data='') to send binary data
        # self.close(code=4123) close with custom error code
        # 1000 code is deafult for code of disconnet
        # text data will use json.dumps

    def disconnect(self, code):
        print('disconnected')

class MyASync(AsyncWebsocketConsumer):

    async def connect(self):
        print('connected')
        await self.accept()
        

    async def receive(self, text_data=None, bytes_data=None):
        print('recieve')  
        for i in range(10):
            await self.send(text_data=str(i))  
            await asyncio.sleep(1)    
        

    async def disconnect(self, code):
        print('disconnected')        

#########################################################################################################################


################ CHAT2

class Chat2MyASync(AsyncWebsocketConsumer):

    async def connect(self):
        self.gp = self.scope['url_route']['kwargs']['gpn']
        await self.channel_layer.group_add(self.gp,self.channel_name)
        await self.accept()
        

    async def receive(self, text_data=None, bytes_data=None):
        print('recieve')  
        d = json.loads(text_data)
        msg = d['mg']
        await self.channel_layer.group_send(self.gp,{
                'type':'chat.message',
                'message':msg
            })

    async def chat_message(self,event):
        # event  = {'type':'chat.message','message':json.dumps(msg)}
        await self.send(text_data=json.dumps({'msg':event['message']}))


    async def disconnect(self, code):
        print('disconnected')    






#############################################################################

# Basic Json

from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer

class J(JsonWebsocketConsumer):

    def connect(self):
        print('Coonect')
        self.accept()

    def receive_json(self, content, **kwargs):
        # here data from frontend postman needs to be send in json formant and it will automaically convert that to dict
        print('recieve')
        # delf.close() force close the connection
        # self.send_json({'msg':'message from DJ'})
        for i in range(10):
            self.send_json({'msg':str(i)})

    def disconnect(self, code):
        print('Dsiconnect code is 1006')

class AJ(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print('Coonect')
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print('recieve')
        # await self.send_json({'msg':'message from DJ'})
        await self.channel_layer.group_send(self.gp,{
                'type':'chat.message',
                'message':content['message']
            })

    async def chat_message(self,event):
        await self.send_json({'message':event['message']})    

    async def disconnect(self, code):
        print('Dsiconnect code is 1006')   
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )


############################################################################################################


