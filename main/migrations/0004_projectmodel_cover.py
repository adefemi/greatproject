# Generated by Django 3.1.4 on 2023-10-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20231015_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='cover',
            field=models.ImageField(null=True, upload_to='project_hub'),
        ),
    ]
