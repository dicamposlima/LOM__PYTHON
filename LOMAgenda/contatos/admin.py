from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'show')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'show')
    list_per_page = 10


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
