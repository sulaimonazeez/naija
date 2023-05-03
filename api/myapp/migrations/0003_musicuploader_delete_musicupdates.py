# Generated by Django 4.1.7 on 2023-03-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_musicupdates_delete_musicupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='musicUploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=255)),
                ('dates', models.CharField(max_length=255)),
                ('albums', models.ImageField(upload_to='myapp/static')),
                ('songs', models.FileField(upload_to='myapp/static')),
            ],
        ),
        migrations.DeleteModel(
            name='musicUpdates',
        ),
    ]
