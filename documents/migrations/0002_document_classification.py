# Generated by Django 3.2.7 on 2021-10-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='classification',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]