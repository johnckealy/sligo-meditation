# Generated by Django 3.1.6 on 2021-02-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
