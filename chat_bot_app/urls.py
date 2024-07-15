from django.urls import path
from .views import chat_view, chatbot_ajax

urlpatterns = [
    path('', chat_view, name='chat_view'),
    path('chatbot_ajax/', chatbot_ajax, name='chatbot_ajax'),
]

