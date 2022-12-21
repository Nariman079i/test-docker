from django.db.models import *
from users.models import *
from users.admin import admin
User = DefaultUser
# Create your models here.

class Bussinesman(Model):

    user = OneToOneField(User, on_delete=CASCADE, related_name="buss")
    inn = CharField(max_length=12, blank=True, null=False )
    call_number = CharField(max_length=60, blank=True, null=False)

    avatar = ImageField(upload_to='picture/avatar/', null=True)

    name = CharField(max_length=60, blank=True, null=False)
    surname = CharField(max_length=60, blank=True, null=False)
    birth_date = DateField(blank=True, null=False)

    locate = CharField(max_length=255, blank=True, null=False)
    industry = CharField(max_length=255, blank=True, null=False)
    sub_industry = CharField(max_length=255, blank=True, null=False)

    status = CharField(max_length=60, blank=True, null=False)
    gender = CharField(max_length=12, blank=True, null=False)

    role = CharField(max_length=12, default="buss",editable=False)
    class Meta:
        verbose_name = "Предприниматель"
        verbose_name_plural = "Предприниматели"

    def __str__(self):
        return f"{self.name} {self.surname} {self.inn}"

class Company(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="com")
    inn = CharField(max_length=12, blank=True, null=False)
    call_number = CharField(max_length=60, blank=True, null=False)

    avatar = ImageField(upload_to='picture/avatar/', null=True)

    name = CharField(max_length=60, blank=True, null=False)
    create_date = DateField(blank=True, null=False, )

    locate = CharField(max_length=255, blank=True, null=False)
    industry = CharField(max_length=255, blank=True, null=False)
    sub_industry = CharField(max_length=255, blank=True, null=False)

    status = CharField(max_length=60, blank=True, null=False)


    role = CharField(max_length=12, default="com",editable=False)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name} {self.inn}"


admin.site.register(Company)
admin.site.register(Bussinesman)