from django.db import models
from django.core.validators import RegexValidator


class Register(models.Model):#por defecto hay un campo null en cada columna y esta en false,si lo cambio a null=true quiere decir que el campo puede quedar en blanco

    YEAR_IN_SCHOOL_CHOICES = (
        (1, '1ro'),
        (2, '2do'),
        (3, '3ro'),
        (4, '4to'),
        (5, '5to')
    )

    created_on = models.DateTimeField(auto_now_add=True)#parametro que activa el date time en el momento de la creacion del objeto
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dni = models.CharField(max_length=8,
                           validators=[RegexValidator(r"^\d{8}$")])
    school_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,
                             validators=[RegexValidator(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")])
    year_in_school = models.IntegerField(choices=YEAR_IN_SCHOOL_CHOICES,default=1)

    def __str__(self):#representacion en string del objeto
        return self.name


class Contact(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)#parametro que activa el date time en el momento de la creacion del objeto
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,
                             validators=[RegexValidator(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",'Ingrese un email válido')])
    message = models.TextField()

    def __str__(self):#representacion en string del objeto
        return self.name

