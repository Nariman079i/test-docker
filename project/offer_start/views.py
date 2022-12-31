from rest_framework.views import APIView
from rest_framework.permissions import *
from users.serializers import *
from users.models import *
from rest_framework.generics import *
from offer_start.serializers import *
from rest_framework.response import Response




class BusinessListAPI(ListAPIView):
    serializer_class = PersonBusinessSerializerList
    queryset = Business.objects.all()
    permission_classes = (AllowAny,)


class InvestorListAPI(ListAPIView):
    serializer_class = PersonInvestorSerializerList
    queryset = Investor.objects.all()
    permission_classes = (AllowAny,)

class BusinessCreateAPI(CreateAPIView):
    serializer_class = PersonBusinessSerializerCreate
    queryset = Business.objects.all()
    permission_classes = [IsAuthenticated, ]

class InvestorCreateAPI(CreateAPIView):
    serializer_class = PersonInvestorSerializerCreate
    queryset = Investor.objects.all()
    permission_classes = [IsAuthenticated, ]


class UserCreateAPI(ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = DefaultUser.objects.all()
    permission_classes = [AllowAny, ]


class TestRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({"is Authenticated": True})

class PersonAccountBusinessAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PersonBusinessSerializerList

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return Business.objects.filter(user=self.request.user)

class PersonAccountInvestorAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PersonInvestorSerializerList

    def get_queryset(self):
        return Investor.objects.filter(user=self.request.user)



