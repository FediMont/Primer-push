# Generated by Django 4.0.4 on 2022-06-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NuevaApp', '0002_remove_bibliotecas_description_bibliotecas_apertura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliotecas',
            name='apertura',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bibliotecas',
            name='link',
            field=models.CharField(max_length=100),
        ),
    ]
