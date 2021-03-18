from django.forms import *
from .models import *

class  ContactFormForm(ModelForm):
    class Meta:
        model = ContactFormUs
        fields = ['name', 'phone', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'field__input', 'placeholder': 'Your name'}),
            'phone': TextInput(attrs={'class': 'field__input', 'placeholder': 'Your phone'}),
            'subject': TextInput(attrs={'class': 'field__input', 'placeholder': 'Title of subject'}),
            'message': Textarea(attrs={'class':'field__textarea', 'placeholder': 'Write your message here.'}),
        }

    # name = forms.CharField(max_length=100, label='Name: ')
    # email = forms.EmailField(label='email')
    # subject = forms.CharField(max_length=100, label='subject', required=False)
    # message = forms.CharField(widget=forms.Textarea, required=True, label='message')

