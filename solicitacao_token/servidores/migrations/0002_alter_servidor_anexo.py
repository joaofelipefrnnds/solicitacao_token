# Generated by Django 4.2 on 2023-05-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='anexo',
            field=models.FileField(null=True, upload_to='static/solicitante_imgs/'),
        ),
    ]
