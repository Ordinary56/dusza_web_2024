# Generated by Django 5.1.3 on 2024-11-10 09:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.IntegerField(choices=[(0, 'CSAPAT'), (1, 'SZERVEZŐ'), (2, 'ISKOLA')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProgLangs',
            fields=[
                ('language', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('term', models.CharField(max_length=20)),
                ('extraMember', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=255)),
                ('schoolAddress', models.CharField(max_length=255)),
                ('principalName', models.CharField(max_length=255)),
                ('principalEmail', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=30)),
                ('mentor', models.CharField(max_length=30)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dusza_app.school')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
