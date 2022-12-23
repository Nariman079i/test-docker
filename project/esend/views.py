import random
from smtplib import SMTPDataError

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from random import randint as rid

class EmailСonfirmation(APIView):
    permission_classes = (AllowAny,)
    def post(self, request,email):
        try:
            code = rid(111111,999999)
            email = self.kwargs.get('email')
            a_email = [email]
            msg = render_to_string('esend/index.html', {'code': code})
            send_mail('Offer - Подтверждение аккаунта',
                      msg,
                      settings.EMAIL_HOST_USER,
                      a_email,
                      html_message=msg)
            return Response({"CODE":code})
        except SMTPDataError as Sm:
            return Response({"ERROR":"Такого пользователя не существует"})
