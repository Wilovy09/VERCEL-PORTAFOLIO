# Generated by Django 4.2.7 on 2023-11-08 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='socialMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(upload_to='social/images')),
                ('Link', models.URLField(blank=True)),
            ],
        ),
    ]