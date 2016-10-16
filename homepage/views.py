from django.shortcuts import render
from .form import RegistrationForm, ContactForm


def index(request):
    contact_form = ContactForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request, 'homepage/home.html',
                {'msg': ('Hola %s, hemos registrado tus datos con éxito' %
                         form.data['name']),
                 'form2': contact_form})
    else:
        form = RegistrationForm()
    return render(request, 'homepage/home.html', {'form': form,
                                                  'form2': contact_form})


def contact(request):
    registration_form = RegistrationForm
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(
                request, 'homepage/success.html',
                {'msg2': ('Hola %s, hemos recibido tu mensaje' %
                          contact_form.data['name']),
                 'form': registration_form})
    else:
        contact_form = ContactForm()
    return render(
        request,
        'homepage/success.html',
        {'form': registration_form, 'form2': contact_form})
