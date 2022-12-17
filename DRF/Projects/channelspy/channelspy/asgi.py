"""
ASGI config for channelspy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelspy.settings')

# application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from app.consumers import MyConsumer
from app.routing import wss_urlpatterns

# ws_patterns =[
#     path('ws/test/',MyConsumer)
# ]

# application = ProtocolTypeRouter({
#     "http":get_asgi_application(),
#     "websocket": AuthMiddlewareStack(URLRouter(wss_urlpatterns))
# })

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": URLRouter(wss_urlpatterns)
})