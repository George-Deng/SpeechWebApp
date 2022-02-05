from rest_framework import serializers
from cmpt_340.backend.buddy_guyAI_api.buddy_guyAI_api.models import Patient
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Resoponse, Response
from .serializers import PatientSerializer

from .models import Patient

@api_view(['GET'])
def apiOverview(request):


    return Response("API BASEPOINT", safe = False)

@api_view(['GET'])
def patientList(request):
    paitents = Patient.objects.all()
    serializer = PatientSerializer(paitents, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def patientCreate(request):
    serializer = PatientSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def patientUpdate(request, primary_key):
    patient = Patient.objects.get(id= primary_key)
    serializer = PatientSerializer(instance = patient, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

@api_view(['DELETE'])
def patientDelete(request, primary_key):
    patient = Patient.objects.get(id= primary_key)
    patient.delete()
    return Response('Deleted')    