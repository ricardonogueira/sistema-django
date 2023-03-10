# Generated by Django 4.1.5 on 2023-01-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('altura', models.FloatField(verbose_name='Altura')),
                ('data_nascimento', models.DateField(null=True, verbose_name='Data de Nascimento')),
            ],
        ),
    ]
