# Generated by Django 4.1.7 on 2023-03-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_musicuploader_delete_musicupdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='musicUploaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=255)),
                ('dates', models.CharField(max_length=255)),
                ('artists', models.CharField(max_length=255)),
                ('albums', models.ImageField(upload_to='myapp/static')),
                ('songs', models.FileField(upload_to='myapp/static')),
            ],
        ),
        migrations.DeleteModel(
            name='musicUploader',
        ),
    ]
