# Generated by Django 4.0.5 on 2022-06-10 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_usuarios_passs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(max_length=500, verbose_name='Descripcion del producto'),
        ),
    ]
