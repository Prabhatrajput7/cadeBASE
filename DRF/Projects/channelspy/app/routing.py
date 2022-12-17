from django.urls import path
from . import consumers


wss_urlpatterns = [
    # path('ws/sc/',consumers.MyC.as_asgi()),
    # path('ws/asc/',consumers.AMyC.as_asgi()),


    # path('ws/sc/<str:gpn>/',consumers.ChatappSync.as_asgi()),
    # path('ws/ac/<str:gpn>/',consumers.ChatappASync.as_asgi()),

    
    # path('ws/sc/',consumers.MySync.as_asgi()),
    # path('ws/ac/',consumers.MyASync.as_asgi()),


    # path('ws/ac/<str:gpn>/',consumers.Chat2MyASync.as_asgi()),

    path('ws/sc/',consumers.J.as_asgi()),

    
]
