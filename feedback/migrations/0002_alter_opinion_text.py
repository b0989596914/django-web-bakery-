# Generated by Django 4.0 on 2022-01-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
