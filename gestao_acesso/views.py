from django.shortcuts import render
from .serializers import AccessRequestSerializer, UsuarioInfoSerializer, LogAcessSerializer # Adicionar LogAcessSerializer se for retornar o log criado
from rest_framework.views import APIView, Response, status
from rest_framework import generics
from .models import Usuario, LogAcess

class VerificarAcessoView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AccessRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        card_id_recebido = serializer.validated_data['cardId']
        log = LogAcess()
        log.card_id = card_id_recebido

        try:
            
            usuario = Usuario.objects.get(cardId=card_id_recebido, is_active=True)
            status_acesso = "Permitido"
            acesso_permitido = True
            usuario_info = UsuarioInfoSerializer(usuario).data # Pega os dados do usuário
        except Usuario.DoesNotExist:
            status_acesso = "Negado - Cartão desconhecido"
            acesso_permitido = False
            usuario_info = None
        
        
        print(log.status)
        log.status = status_acesso
        log.save()

        if acesso_permitido:
        
            return Response({
                'status': status_acesso,
                'message': 'Acesso Permitido',
                'usuario': usuario_info # Retorna info do usuário
            }, status=status.HTTP_200_OK)
            
        else:
            return Response({
                'status': status_acesso,
                'message': 'Acesso Negado'
            }, status=status.HTTP_403_FORBIDDEN)
            

class LogAcessListView(generics.ListAPIView):
    queryset = LogAcess.objects.all()
    serializer_class = LogAcessSerializer
    # Adicionar permissões se necessário (ex: IsAdminUser)
    
class CadastrarCartaoView(APIView):
    def post(self, request, usuario_id,*args, **kwargs):
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
        except:
            return Response({'erro':'usuario nao encotrado!!'})
        
        card_id_novo = request.data.get('cardId')
        
        if not card_id_novo:
            return Response({'error': 'cardId é obrigatório'})
        
        if hasattr(usuario, 'cardId'):
            usuario.cardId = card_id_novo
            usuario.save()
            return Response({'message': f"Cardao {card_id_novo} salvo para o usuario com email: {usuario.email}"})