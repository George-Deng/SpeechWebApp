#serializers create model object based on defined variables
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import CustomUser, Doctor, Patient
from upload.models import Upload, Annotation
from upload.models import Upload
from api.models import UploadPrediction
from rest_framework.validators import UniqueValidator
from django.forms.models import model_to_dict
import json
from django.db.models import Min, Max, Q, Count

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        allow_null=True,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
                message="This email is already taken!",
            )
        ],
    )
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "user_type")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(
            **validated_data
        )  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class GetCurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["email", "user_type"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["email", "user_type"]

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation 
        fields = "__all__"
class UploadPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadPrediction
        fields = "__all__"
#gets, validates, and creates token pair (Access and Refresh)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # Add extra responses here
        #data["contact_number"] = self.user.contact_number
        data["email"] = self.user.email
        data["user_id"] = self.user.pk
        if hasattr(self.user, "profile"):
            data["profile"] = {**model_to_dict(self.user.profile)}
        return data

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        #token["contact_number"] = user.contact_number
        token["email"] = user.email
        return token

