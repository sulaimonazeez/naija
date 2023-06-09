# Generated by Django 4.1.7 on 2023-03-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='musicUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('album', models.ImageField(upload_to='myapp/static')),
                ('song', models.FileField(upload_to='myapp/static')),
            ],
        ),
        migrations.DeleteModel(
            name='musicUpdate',
        ),
    ]
