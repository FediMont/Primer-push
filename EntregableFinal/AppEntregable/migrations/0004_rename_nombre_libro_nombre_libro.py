# Generated by Django 4.0.4 on 2022-06-08 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregable', '0003_libro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='nombre',
            new_name='nombre_libro',
        ),
    ]