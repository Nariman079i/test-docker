from rest_framework.views import APIView
from rest_framework.permissions import *
from users.serializers import *
from users.models import *
from rest_framework.generics import *
from offer_start.serializers import *
from rest_framework.response import Response

class UserBusinessAPI(ListAPIView):
    serializer_class = UsersBusinessSerializer
    queryset =  UsersBusiness.objects.all()
    permission_classes = (AllowAny,)

class UserInvestorAPI(ListAPIView):
    serializer_class = UsersBusinessSerializer
    queryset = UsersInvestor.objects.all()
    permission_classes = (AllowAny,)

class CompanyMainListAPI(ListAPIView):
    serializer_class = PersonCompanySerializerMainList
    queryset = Company.objects.all()
    permission_classes = (AllowAny,)


class BusinessmanMainListAPI(ListAPIView):
    serializer_class = PersonBusinessmanSerializerMainList
    queryset = Bussinesman.objects.all()
    permission_classes = (AllowAny,)

class CompanyListAPI(ListAPIView):
    serializer_class = PersonCompanySerializerList
    queryset = Company.objects.all()
    permission_classes = (AllowAny,)


class BusinessmanListAPI(ListAPIView):
    serializer_class = PersonBusinessmanSerializerList
    queryset = Bussinesman.objects.all()
    permission_classes = (AllowAny,)

class CompanyCreateAPI(CreateAPIView):
    serializer_class = PersonCompanySerializerCreate
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated, ]

class BusinessmanCreateAPI(CreateAPIView):
    serializer_class = PersonBusinessmanSerializerCreate
    queryset = Bussinesman.objects.all()
    permission_classes = [IsAuthenticated, ]


class UserCreateAPI(ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = DefaultUser.objects.all()
    permission_classes = [AllowAny, ]


class TestRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({"is Authenticated": True})

class PersonAccountCompanyAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PersonCompanySerializerList

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return Company.objects.filter(user=self.request.user)

class PersonAccountBusinessmanAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PersonBusinessmanSerializerList

    def get_queryset(self):
        return Bussinesman.objects.filter(user=self.request.user)



