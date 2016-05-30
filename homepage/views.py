from django.shortcuts import render
from .form import RegistrationForm,ContactForm

# Create your views here.

def index(request):
    form2 = ContactForm()
    if request.method == "POST":
        form = RegistrationForm (request.POST)#haciendo post del form
        if form.is_valid():
            form.save()
            return render(request,'homepage/home.html', {'msg':
                form.data['name']+' hemos registrado tus datos con exito','form2':form2})#el html regresa con el mensaje de exito
    else:
        form = RegistrationForm()
    return render(request, 'homepage/home.html', {'form': form, 'form2': form2})

def contact(request):
    formu = RegistrationForm
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'homepage/success.html', {'msg2':form.data['name']+' tu mensaje ha sido enviado','form':formu})
    else:
        form = ContactForm()
    return render(request, 'homepage/success.html', {'form': formu, 'form2': form})
