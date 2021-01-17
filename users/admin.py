from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture') ## Organiza como ver los datos y cuales mostrar en la pagina de admin de DJango

    list_display_links = ('pk','user') ## Da propiedad de link a las columnas dadas

    list_editable = ('phone_number', 'website', 'picture') ## Permite que se puedan editar los datos desde la tabla de lista y no solo al acceder a los detalles

    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number', 'user__username') ## Crea una barra de busqueda que permite buscar segun los parametros dados

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff') ## Crea un filtro segun los parametros dados

    fieldsets = (  ## Permite modificar(categorizar) el formulario de detalles del perfil y presentarlo de manera deseada
        ('Profile', {
            'fields': (
                ('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (('website', 'phone_number'), 'biography')
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )
    
    readonly_fields = ('created', 'modified', 'user') ## Permite especificar que campos no seran editables


## Profile in-line admin for users
class ProfileInLine(admin.StackedInline):

    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)