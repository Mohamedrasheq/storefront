# Generated by Django 5.0.3 on 2024-04-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('age', models.IntegerField()),
                ('collage', models.TextField()),
                ('placed', models.CharField(max_length=500)),
            ],
        ),
    ]
