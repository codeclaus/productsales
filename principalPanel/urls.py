from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('close', views.close_sesion, name="close"),
    path('logear', views.logear, name="logear"),
]
