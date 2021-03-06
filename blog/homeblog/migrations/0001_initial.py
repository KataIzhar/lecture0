# Generated by Django 3.0.8 on 2020-08-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('time', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=250)),
                ('website', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
