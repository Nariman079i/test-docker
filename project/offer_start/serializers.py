from rest_framework.serializers import *
from offer_start.models import *
from users.serializers import UserCreateSerializer


class PersonBusinessSerializerCreate(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Business
        fields = "__all__"

    def validate(self, data):
        if Business.objects.filter(user=data['user']).exists():
            raise ValidationError(
                {
                    'error': 'Такой пользователь уже зарегистрирован'
                }
            )

        for k in data:
            if k == "avatar":
                continue

            elif not data[k] or data[k] == "":
                raise ValidationError({
                    k: "Поле не может быть пустым"
                })
        try:
            return data

        except KeyError as k:
            raise ValidationError({
                'create_date': str("Введите дату")
            })

        return data


class PersonInvestorSerializerCreate(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Investor
        fields = "__all__"

    def validate(self, data):
        if Investor.objects.filter(user=data['user']).exists():
            raise ValidationError(
                {
                    'error': 'Такой пользователь уже зарегистрирован'
                }
            )
        try:
            for k in data:
                if k == "avatar":
                    continue
                if not data[k] or data[k] == "":
                    raise ValidationError({
                        k: "Поле не может быть пустым"
                    })
            return data

        except KeyError as k:
            raise ValidationError({
                'birth_date': str("Введите дату")
            })

        return data


class PersonInvestorSerializerList(ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = Investor
        fields = "__all__"


class PersonBusinessSerializerList(ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = Business
        fields = "__all__"


