# Generated by Django 3.2.7 on 2021-09-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=240)),
                ('url', models.CharField(max_length=240)),
                ('title', models.CharField(max_length=240)),
                ('content', models.CharField(max_length=2000)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=240)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
