from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "form_full_name", "placeholder":"Your Full Name"}))
    email    = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "id": "form", "placeholder":"Your Email"}))
    message  = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "form_content", "placeholder":"Your Message Here"})) 

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be Gmail!")
            return email
    
    def clean_content(self):
        raise forms.ValidationError("Content is wrong.")