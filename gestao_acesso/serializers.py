# gestao_acesso/serializers.py

from rest_framework import serializers
from django.utils import timezone # Para o LogAcessSerializer, se necessário
from .models import Usuario, LogAcess

class AccessRequestSerializer(serializers.Serializer):
    """
    Serializer para validar o cardId recebido do ESP32.
    Não está ligado a um modelo diretamente, apenas valida o dado de entrada.
    """
    cardId = serializers.CharField(max_length=100, required=True)

    def validate_cardId(self, value):
        # Você pode adicionar validações customizadas para o formato do cardId aqui, se necessário
        if not value.isalnum(): # Exemplo: verificar se é alfanumérico
            raise serializers.ValidationError("Card ID deve ser alfanumérico.")
        return value


class UsuarioInfoSerializer(serializers.ModelSerializer):
    """
    Serializer para exibir informações básicas do usuário.
    Útil para retornar quem acessou, caso o ESP32 precise dessa informação
    ou para uma interface de administração.
    """
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'cardId', 'is_active'] # Campos que você quer expor


class LogAcessSerializer(serializers.ModelSerializer):
    """
    Serializer para criar e listar os logs de acesso.
    """
    class Meta:
        model = LogAcess
        fields = ['id', 'card_id', 'timestamp', 'status']
        read_only_fields = ['timestamp'] # Timestamp é definido automaticamente

    # Se você quisesse permitir a criação de logs via API diretamente (além da criação automática na view de verificação)
    # você poderia adicionar um método create aqui ou apenas usar o ModelSerializer como está.
    # Para a sua view VerificarAcessoView, a criação do log é feita manualmente, o que é bom,
    # mas este serializer seria útil para listar logs em outro endpoint, por exemplo.

# --- Serializers mais completos para CRUD de Usuários (Opcional para o ESP32, mais para admin) ---

class UsuarioCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criar novos usuários, lidando com a senha corretamente.
    """
    # Definir email como obrigatório na criação, mesmo que não esteja em REQUIRED_FIELDS no modelo
    # (embora seu manager já cuide disso, é bom ter no serializer também)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    cardId = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)


    class Meta:
        model = Usuario
        fields = ['email', 'password', 'cardId', 'is_active', 'is_staff'] # Adicione outros campos conforme necessário

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            cardId=validated_data.get('cardId'), # Usa .get() pois pode não estar presente
            is_active=validated_data.get('is_active', True),
            is_staff=validated_data.get('is_staff', False)
        )
        return user

class UsuarioDetailSerializer(serializers.ModelSerializer):
    """
    Serializer para detalhar e atualizar usuários.
    """
    # Para atualização, não queremos exigir a senha toda vez,
    # nem queremos expor a senha hasheada.
    # A atualização de senha geralmente é um endpoint separado.
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'cardId', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined'] # date_joined e last_login são da AbstractBaseUser
        read_only_fields = ['last_login', 'date_joined', 'is_superuser'] # is_superuser geralmente é gerenciado pelo create_superuser
        
