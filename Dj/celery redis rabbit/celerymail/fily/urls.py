from django.urls import path
from . import views

urlpatterns = [
    path('',views.upload_file),
     path('<task_id>' , views.check_status , name="check_status"),
]
