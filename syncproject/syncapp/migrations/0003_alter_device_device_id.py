# Generated by Django 5.1 on 2024-09-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syncapp', '0002_user_remove_device_name_device_device_id_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
