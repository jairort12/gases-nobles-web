from modeltranslation.translator import register, TranslationOptions
from .models import Servicio

# Le decimos que el modelo Servicio tendrá traducciones
@register(Servicio)
class ServicioTranslationOptions(TranslationOptions):
    # ¿Qué campos queremos traducir? (El identificador no, porque es para la URL)
    fields = ('nombre', 'descripcion')