# Generated by Django 5.0 on 2023-12-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
