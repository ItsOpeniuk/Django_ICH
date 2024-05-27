from django.urls import path
from users.views import greet

urlpatterns = [
    path('<str:user_name>', greet, name='greet')
]