# Generated by Django 4.1.4 on 2023-01-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EID', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=50)),
                ('ESAL', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('SID', models.IntegerField(primary_key=True, serialize=False)),
                ('SNAME', models.CharField(max_length=100)),
                ('SMAIL', models.EmailField(max_length=50)),
                ('SMARKS', models.IntegerField()),
                ('SAGE', models.IntegerField(max_length=2)),
            ],
        ),
    ]
