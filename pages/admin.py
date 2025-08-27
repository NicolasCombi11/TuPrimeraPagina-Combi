from django.contrib import admin
from .models import Page
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','creado')
    search_fields = ('titulo','bajada','contenido')
    list_filter = ('creado',)
