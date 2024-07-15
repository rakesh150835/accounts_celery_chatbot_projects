from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Message
from .utils import get_response_from_model



def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('query')
        if user_message is not None:
        
            bot_response = get_response_from_model(user_message)

            Message.objects.create(user=request.user, message=user_message, response=bot_response)
            return redirect('chat_view')
    
    messages = Message.objects.filter(user=request.user).order_by('-timestamp')
    
    context = {
            'messages': messages
        }
    
    return render(request, 'chat_bot_app/chat_bot_1.html', context)



def chatbot_ajax(request):
    if request.method == 'POST':
        user_message = request.POST.get('query')

        if user_message is not None:
            bot_response = get_response_from_model(user_message)

            Message.objects.create(user=request.user, message=user_message, response=bot_response)
            
            data = {
                'response': bot_response,
            }
            
            return JsonResponse(data)
