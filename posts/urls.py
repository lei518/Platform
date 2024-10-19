from django.urls import path
from .views import register, approve_user

urlpatterns = [
    path('register/', register, name='register'),
    path('approve/<int:user_id>/', approve_user, name='approve_user'),
]
