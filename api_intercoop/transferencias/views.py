from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transferencia
from .serializers import TransferenciaSerializer
from django.utils import timezone

@api_view(['POST'])
def crear_transferencia(request):
    data = request.data
    data['comision'] = 0.41
    serializer = TransferenciaSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'mensaje': 'Transferencia registrada correctamente.', 'datos': serializer.data})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def confirmar_transferencia(request):
    id = request.data.get('id')
    try:
        transferencia = Transferencia.objects.get(id=id)
        transferencia.estado = 'completada'
        transferencia.fecha_confirmacion = timezone.now()
        transferencia.save()
        return Response({'mensaje': 'Transferencia confirmada'})
    except Transferencia.DoesNotExist:
        return Response({'error': 'Transferencia no encontrada'}, status=404)

@api_view(['GET'])
def transferencias_pendientes(request):
    coop = request.query_params.get('coop')
    transferencias = Transferencia.objects.filter(cooperativa_destino=coop, estado='pendiente')
    serializer = TransferenciaSerializer(transferencias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def transferencias_confirmadas(request):
    coop = request.query_params.get('coop')
    transferencias = Transferencia.objects.filter(cooperativa_destino=coop, estado='completada')
    serializer = TransferenciaSerializer(transferencias, many=True)
    return Response(serializer.data)