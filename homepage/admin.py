from django.contrib import admin
from homepage.models import Register, Contact


class RegisterAdmin(admin.ModelAdmin):

    list_display = ('name', 'last_name', 'school_name', 'created_on', 'site')
    ordering = ('-created_on',)
    list_filter = ('site',)


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'created_on', 'answered_by')
    list_filter = ('answered_by',)
    ordering = ('-created_on',)


admin.site.register(Register, RegisterAdmin)
admin.site.register(Contact, ContactAdmin)
