from rest_framework.serializers import *

from users.models import DefaultUser
class UserCreateSerializer(ModelSerializer):
    email = EmailField(style={'input_type':'email'})
    password = CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = DefaultUser
        fields = ("email","password")

    def create(self, validated_data):

        if DefaultUser.objects.filter(email=validated_data.get('email')).exists():
            raise ValidationError({"error":"Такой пользователь уже существует"})
        user = DefaultUser.objects.create_user(**validated_data)
        return user

