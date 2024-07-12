from django.shortcuts import render, redirect
from .forms import ChatForm
from .models import Message
from .utils import get_response_from_model



def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            
            bot_response = get_response_from_model(user_message)

            Message.objects.create(user=request.user, message=user_message, response=bot_response)
            return redirect('chat_view')
    else:
        form = ChatForm()

    messages = Message.objects.filter(user=request.user).order_by('-timestamp')
    
    context = {
            'form': form, 
            'messages': messages
        }
    
    return render(request, 'chat_bot_app/chat_bot_1.html', context)