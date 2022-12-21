# Generated by Django 4.1.4 on 2022-12-20 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer_start', '0009_remove_bussinesman_avatar_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='picture/default_avatar')),
            ],
        ),
        migrations.AddField(
            model_name='bussinesman',
            name='avatar_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='offer_start.image'),
        ),
        migrations.AddField(
            model_name='company',
            name='avatar_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='offer_start.image'),
        ),
    ]