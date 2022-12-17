from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/notification/', consumers.NotificationConsumer.as_asgi()),
    # path('ws/notification/<room_name>', consumers.NotificationConsumer.as_asgi()),
]