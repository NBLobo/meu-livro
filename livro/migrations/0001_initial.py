# Generated by Django 3.1.5 on 2021-03-26 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('resenha', models.TextField(max_length=1000)),
            ],
        ),
    ]
