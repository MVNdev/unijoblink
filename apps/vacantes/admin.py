from django.contrib import admin
from .models import Area, Image, Vacante, Perfil, Postulados
from django.utils.translation import ngettext
from django.contrib import messages

# Register your models here.
@admin.register(Vacante)
class VacanteAdmin(admin.ModelAdmin):
    list_display = ["nombreEmpresa", "nombreVacante", "area", "slug", "visible"]
    list_editable = ["nombreVacante", "area", "slug", "visible",]
    search_fields = ("nombreEmpresa", "nombreVacante")
    list_filter = ["nombreEmpresa", "nombreVacante", "area", "visible"]
    list_per_page = 10
    list_display_links = ["nombreEmpresa",]
    actions = ['Disponible', 'NoDisponible']

    @admin.action(description='Disponible')
    def Disponible(self, request, queryset):
        updated = queryset.update(visible=True)
        self.message_user(request, ngettext(
            '%d vacante esta disponible.',
            '%d vacantes estan disponibles.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='No disponible')
    def NoDisponible(self, request, queryset):
        updated = queryset.update(visible=False)
        self.message_user(request, ngettext(
            '%d vacante dejo de estar disponible.',
            '%d vacantes dejaron de estar disponibles.',
            updated,
        ) % updated, messages.SUCCESS)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass

@admin.register(Postulados)
class PostuladosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area)
# admin.site.register(Image)