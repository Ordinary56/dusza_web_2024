# Generated by Django 5.1.3 on 2024-11-09 19:25

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dusza_app', '0006_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator('^[\\w @+.-]+$', 'Enter a valid username. This value may contain only letters, numbers, spaces, and @/./+/-/_ characters.')]),
        ),
    ]
