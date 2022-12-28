
from django.db.models import *

from django.contrib.auth.models import BaseUserManager , AbstractBaseUser


class DefaultUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Обязательное поле")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email , password=None):
        if not email:
            raise ValueError('Поле почты не должно быть пустым')
        email = self.normalize_email(email)
        user = self.model(email=email)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user


class DefaultUser(AbstractBaseUser):
    email = EmailField('email', unique=True)

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    date_joined = DateField(auto_now_add=True)
    last_login = DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = DefaultUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UsersBusiness(Model):
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

class UsersInvestor(Model):

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
