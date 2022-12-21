from rest_framework.serializers import *
from offer_start.models import *
from users.serializers import UserCreateSerializer


class PersonCompanySerializerCreate(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Company
        fields = "__all__"

    def validate(self, data):
        if Company.objects.filter(user=data['user']).exists():
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


class PersonBusinessmanSerializerCreate(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Bussinesman
        fields = "__all__"

    def validate(self, data):
        if Bussinesman.objects.filter(user=data['user']).exists():
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


class PersonBusinessmanSerializerList(ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = Bussinesman
        fields = "__all__"


class PersonCompanySerializerList(ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

class PersonBusinessmanSerializerMainList(ModelSerializer):
    class Meta:
        model = Bussinesman
        fields = ('avatar','name', 'surname', 'industry', 'locate', 'status')

class PersonCompanySerializerMainList(ModelSerializer):

    class Meta:
        model = Company
        fields = ('avatar','name', 'surname', 'industry', 'locate', 'status')
