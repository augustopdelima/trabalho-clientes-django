from django.contrib import admin

from clientes.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'cidade', 'created_at']
    search_fields = ['nome', 'sobrenome']
    list_filter = ['nome', 'sobrenome']