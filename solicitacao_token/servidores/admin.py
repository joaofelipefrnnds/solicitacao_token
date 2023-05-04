from django.contrib import admin
from .models import *

admin.site.register(Coordenadoria),
admin.site.register(Departamento),
admin.site.register(Cargo),


class ServidorAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','rg','telefone' ,'status', 'cadastrado_em')
    list_filter = ("fk_cargo", "fk_coordenadoria", "fk_departamento") #adiciona um filtro por categoria
   # list_editable = ('status',)
admin.site.register(Servidor, ServidorAdmin),