from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['subject', 'message']
        widgets = {
            
            'subject': forms.TextInput(attrs={"class": "form-control input-lg", 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Message', 'rows': '4', 'cols':'25', 'style':'height: 170px;' }),
        }
