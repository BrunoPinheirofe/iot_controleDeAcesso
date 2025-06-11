from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Usuario, LogAcess

# Register your models here.


class UsuarioAdmin(UserAdmin):

    model = Usuario
    # list_display = ('email', 'cardId', 'is_staff', 'is_active', 'is_superuser') # Adicione os campos que quer ver
    # fieldsets = UserAdmin.fieldsets + ( # Adiciona o campo cardId aos fieldsets existentes
    #     ('Informações RFID', {'fields': ('cardId',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + ( # Adiciona cardId ao formulário de criação
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('cardId',),
    #     }),
    # )
    # Adapte os fieldsets e list_display conforme sua necessidade,
    # especialmente se você removeu o campo 'username' do modelo Usuario
    # e está usando 'email' como USERNAME_FIELD.
    # O UserAdmin padrão já espera 'username'. Se você o removeu,
    # precisará ajustar mais os fieldsets.
    # Uma abordagem mais simples se 'email' é o username:
    list_display = ["email", "cardId", "is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {"fields": ("cardId",)},
        ),  # Adicione outros campos pessoais se tiver
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),  # date_joined é automático
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password",
                    "password2",
                    "cardId",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ["email"]
    ordering = ["email"]


admin.site.register(Usuario, UsuarioAdmin)

@admin.register(LogAcess) # Outra forma de registrar
class LogAcessAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'timestamp', 'status', 'usuario_email') # Adicione um método para mostrar o email
    readonly_fields = ('timestamp',) # Timestamp não deve ser editável

    def usuario_email(self, obj):
        """Retorna o email do usuário associado ao card_id, se existir."""
        try:
            usuario = Usuario.objects.get(cardId=obj.card_id)
            return usuario.email
        except Usuario.DoesNotExist:
            return None

    list_filter = ('status', 'timestamp')
    search_fields = ('card_id',)

