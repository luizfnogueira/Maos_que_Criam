# Generated by Django 5.1.1 on 2024-10-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app15', '0005_doador_email_doador_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('opiniao', models.TextField()),
                ('avaliacao', models.CharField(max_length=20)),
            ],
        ),
    ]
