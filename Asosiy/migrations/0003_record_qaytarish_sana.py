# Generated by Django 5.0.1 on 2024-01-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0002_talaba_kitob_soni'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='qaytarish_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]