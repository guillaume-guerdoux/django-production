from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('send-email', views.send_email, name='send_email'),
]
