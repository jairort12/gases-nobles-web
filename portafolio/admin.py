from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(TranslationAdmin):
    pass