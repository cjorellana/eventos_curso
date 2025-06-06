from django.contrib import admin
from .models import evento
# Register your models here.

@admin.register(evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('ID', 'nombre', 'fecha_Inicio', 'fecha_fin', 'precio', 'diploma', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo', 'diploma')
    ordering = ('-fecha_Inicio',)
    date_hierarchy = 'fecha_Inicio'
    
    fieldsets = (
        (None, {
            'fields': ('nombre', 'description')
        }),
        ('Fechas', {
            'fields': ('fecha_Asig', 'fecha_Inicio', 'fecha_fin', 'fecha_fin_asig')
        }),
        ('Detalles Financieros', {
            'fields': ('precio',)
        }),
        ('Configuración', {
            'fields': ('diploma', 'activo')
        }),
        ('Multimedia', {
            'fields': ('image',)
        }),
    )