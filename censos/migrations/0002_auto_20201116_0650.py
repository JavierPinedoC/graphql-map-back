# Generated by Django 3.1.3 on 2020-11-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('censos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='censo',
            name='actividad',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='censo',
            name='estado',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='censo',
            name='idestado',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='censo',
            name='idmunicipio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='censo',
            name='municipio',
            field=models.TextField(null=True),
        ),
    ]
