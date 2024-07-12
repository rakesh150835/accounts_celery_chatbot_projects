from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={"size": 10, "title": "Your name", 'placeholder':"Type here..."}))