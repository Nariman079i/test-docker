# Generated by Django 4.1.4 on 2022-12-19 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offer_start', '0003_alter_person_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bussinesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(blank=True, max_length=12)),
                ('call_number', models.CharField(blank=True, max_length=60)),
                ('avatar', models.ImageField(null=True, upload_to='img/')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('surname', models.CharField(blank=True, max_length=60)),
                ('birth_date', models.DateField(blank=True)),
                ('locate', models.CharField(blank=True, max_length=255)),
                ('industry', models.CharField(blank=True, max_length=255)),
                ('sub_industry', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, max_length=60)),
                ('gender', models.CharField(blank=True, max_length=12)),
                ('role', models.CharField(choices=[('inv', 'inv'), ('buss', 'buss')], max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Предприниматель',
                'verbose_name_plural': 'Предприниматели',
            },
        ),
        migrations.CreateModel(
            name='Compnany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(blank=True, max_length=12)),
                ('call_number', models.CharField(blank=True, max_length=60)),
                ('avatar', models.ImageField(null=True, upload_to='img/')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('surname', models.CharField(blank=True, max_length=60)),
                ('birth_date', models.DateField(blank=True)),
                ('locate', models.CharField(blank=True, max_length=255)),
                ('industry', models.CharField(blank=True, max_length=255)),
                ('sub_industry', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, max_length=60)),
                ('gender', models.CharField(blank=True, max_length=12)),
                ('role', models.CharField(choices=[('inv', 'inv'), ('buss', 'buss')], max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='com', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='picture/default_avatar')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]