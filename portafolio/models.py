from django.db import models
from ckeditor.fields import RichTextField

class Servicio(models.Model):
    # Este será el texto corto para la URL (ej. 'hidrogeno')
    identificador = models.CharField(max_length=50, unique=True)
    
    # El título que verá el cliente
    nombre = models.CharField(max_length=100)
    
    # El texto largo que explica el área de trabajo
    descripcion = RichTextField()

    # Campo para subir una imagen representativa del servicio

    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)


    # Esto hace que en el panel de administrador veamos el nombre real en vez de "Servicio Object 1"
    def __str__(self):
        return self.nombre
