from django.urls.conf import path
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from offer_start.views import *
from esend.views import *
urlpatterns = [
    path('account/com/', PersonAccountCompanyAPI.as_view()),
    path('account/bus/', PersonAccountBusinessmanAPI.as_view()),
    path('create/', UserCreateAPI.as_view()),

    path('create/bus/', BusinessmanCreateAPI.as_view()),
    path('create/com/', CompanyCreateAPI.as_view()),

    path('list/com/', CompanyListAPI.as_view()),
    path('list/bus/', BusinessmanListAPI.as_view()),

    path('list/bus/main/', BusinessmanMainListAPI.as_view()),
    path('list/com/main/', CompanyMainListAPI.as_view()),

    path('test/',TestRegistration.as_view()),
    path('email/confirmation/<str:email>/', EmailСonfirmation.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]