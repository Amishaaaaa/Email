from django.urls import path
from .views import *

urlpatterns = [
    path('api/send/mail', SendMail.as_view(), name='send-mail'),
]