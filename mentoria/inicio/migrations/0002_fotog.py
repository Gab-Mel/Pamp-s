# Generated by Django 3.2.5 on 2021-12-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fotog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
                ('foto', models.FileField(upload_to='media/')),
            ],
        ),
    ]
