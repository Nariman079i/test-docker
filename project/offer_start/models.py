from django.db.models import *
from users.models import *
from users.admin import admin
User = DefaultUser
# Create your models here.

class Investor(Model):

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

    role = CharField(max_length=12, default="inv",editable=False)
    class Meta:
        verbose_name = "Инвестор"
        verbose_name_plural = "Инвесторы"

    def __str__(self):
        return f"{self.name} {self.surname} {self.inn}"

class Business(Model):
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


    role = CharField(max_length=12, default="bus",editable=False)

    class Meta:
        verbose_name = "Бизнес"
        verbose_name_plural = "Бизнесы"

    def __str__(self):
        return f"{self.name} {self.inn}"


admin.site.register(Business)
admin.site.register(Investor)