from django.db.models.base import Model
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .predict import predict_gender, predict_parkinsons
from users.models import CustomUser, Doctor, Patient
from upload.models import Upload
from api.models import UploadPrediction
from .serializers import *
from django.forms.models import model_to_dict

from django.db.models import Count, Q

from django.core import serializers
from rest_framework.decorators import api_view

#Gets token pair (Access and Refresh)
class ObtainTokenPairWithEmailView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

#Gets current logged in user
class GetUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

#returns gender prediction based on file id number. This id number represents an audio wav file.
def gender_ai(request, file_pk):
    upload_dict = Upload.objects.all().filter(id=int(file_pk)).values()
    print('https://cmpt-340.s3.amazonaws.com/media/'+upload_dict[0]['file'])
    predict_gender('https://cmpt-340.s3.amazonaws.com/media/'+upload_dict[0]['file'])
    return JsonResponse(predict_gender(upload_dict[0]['file']), safe=False)

#returns parkinsons prediction based on file id number. This id number represents an audio wav file.
def parkinsons_ai(request, file_pk):
    upload_dict = Upload.objects.all().filter(id=int(file_pk)).values()
    print('https://cmpt-340.s3.amazonaws.com/media/'+upload_dict[0]['file'])
    predict_parkinsons('https://cmpt-340.s3.amazonaws.com/media/'+upload_dict[0]['file'])
    return JsonResponse(predict_parkinsons(upload_dict[0]['file']), safe=False)

#get request for a given doctor's patients
@api_view(['GET'])
def get_doctors_patients(request, file_pk):
    doctor = Doctor.objects.get(id = file_pk)
    alldoctorpatients = doctor.patients.all()
    serializer = PatientSerializer(alldoctorpatients, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#get request for a given patient's uploads
@api_view(['GET'])
def get_patients_uploads(request, file_pk):
    patient_id = request.query_params.get("patient_id","")
    doctor = Doctor.objects.get(id = file_pk)
    patients = doctor.patients.all()
    if patient_id != "":
        patients = patients.filter(id = int(patient_id))
    user_details = Upload.objects.filter(patient_id__in=patients.values_list('id', flat=True))
    serializer = UploadSerializer(user_details, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#get and post request for a doctor
class DoctorView(APIView):
    serializer_class = DoctorSerializer
    def get(self, request, *args, **kwargs):
        queryset = Doctor.objects.all()
        id = self.request.query_params.get("id", "")
        if id != "":
            queryset = queryset.filter(id=int(id))
        serializer = DoctorSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format="json"):

        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            upload = serializer.save()
            if upload:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #get and post request for a patient
class PatientView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Patient.objects.all()
        id = self.request.query_params.get("id", "")
        if id != "":
            queryset = queryset.filter(id=int(id))
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format="json"):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            upload = serializer.save()
            if upload:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #get and post request for a new audio file upload.
class UploadView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser]
    def post(self, request, format="json"):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            upload = serializer.save()
            if upload:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format="json"):
        queryset = Upload.objects.all()
        patient_id = self.request.query_params.get("patient_id", "")
        if patient_id != "":
            queryset = queryset.filter(patient_id=int(patient_id))
        serializer = UploadSerializer(queryset, many=True)
        print(serializer.data[0]["file"])
        return Response(serializer.data)
    
#get current user logged in.
class GetCurrentUserView(generics.ListAPIView):
    serializer_class = GetCurrentUserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.filter(pk=self.request.user.pk)
        return queryset

#get post and put request for annotations.
@api_view(['GET', 'POST', 'PUT'])
def annotations_view(request, upload_id, format="json"):
    if request.method == 'GET':
        queryset = Annotation.objects.filter(upload_id=int(upload_id))
        serializer = AnnotationSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnnotationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        annotation = Annotation.objects.get(id = int(request.data.get('id')))
        serializer = AnnotationSerializer(annotation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#creates a new user object for signup.
class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format="json"):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#gets recorded upload predictions
class GetUploadPrediction(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = UploadPrediction.objects.all()
        id = self.request.query_params.get("id","")
        if id != "":
            queryset = queryset.filter(id=int(id))
        serializer = UploadPredictionSerializer(queryset, many=True)
        return Response(serializer.data)

#logout
class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
