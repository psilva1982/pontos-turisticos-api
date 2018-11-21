from .actions import reprova_comentarios
from .models import Comentario
from django.contrib import admin

from comentarios.actions import aprova_comentarios, reprova_comentarios

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]

# Register your models here.
admin.site.register(Comentario, ComentarioAdmin)