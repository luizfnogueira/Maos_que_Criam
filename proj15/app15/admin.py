from django.contrib import admin
from .models import Doacao
from .models import Doador
from .models import Donor
from .models import Donation
from django.urls import reverse
from django.utils.html import format_html
from django.urls import path
from .views import generate_report
from .models import Necessidade

@admin.register(Doacao)

class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo_material', 'quantidade', 'data_doacao', 'doador','produto')
admin.site.register(Doador)

@admin.register(Necessidade)
class NecessidadeAdmin(admin.ModelAdmin):
    list_display = ('item', 'prioridade', 'data_criacao')
    list_filter = ('prioridade', 'data_criacao')
    search_fields = ('item',)
