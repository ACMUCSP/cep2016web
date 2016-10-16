from django import forms

from .models import Register, Contact #importa el modelo Register


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('name', 'last_name', 'dni', 'school_name', 'email',
                  'year_in_school', 'site', 'omegaup_username',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)
