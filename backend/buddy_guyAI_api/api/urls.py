# url paths for different endpoints
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path("upload/", UploadView.as_view()),
    path("upload/predictions/",GetUploadPrediction.as_view()),
    path("patient/", PatientView.as_view()),
    path("patient_uploads/<int:file_pk>/", get_patients_uploads),
    path("gender/<int:file_pk>/",gender_ai),
    path("parkinsons/<int:file_pk>/",parkinsons_ai),
    path("doctor/",DoctorView.as_view()),
    path("doctor/<int:file_pk>/", get_doctors_patients),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/obtain/", ObtainTokenPairWithEmailView.as_view(), name="token_create"), 
    path("annotations/<int:upload_id>", annotations_view, name="get_and_create_annotation"),
    path(
        "token/obtain/", ObtainTokenPairWithEmailView.as_view(), name="token_create"
    ), 
    path('token/blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path("user/create/", CustomUserCreate.as_view(), name="create_user"),
    path("user/<int:pk>/", GetUserView.as_view(), name="get_user"),
    path("user/current/", GetCurrentUserView.as_view(), name="get_current_user"),
]
