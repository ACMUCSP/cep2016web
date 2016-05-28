from django import forms

from .models import Register, Contact #importa el modelo Register

class RegistrationForm(forms.ModelForm):#el nombre del form RegistrationForm necesita hacerse conocer por django mediante ModelForm
    class Meta:
        model = Register #que modelo debe utilizar django para crear este form?
        fields = ('name','last_name','dni','school_name','email','year_in_school',)# campos

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = ('name','email','message',)