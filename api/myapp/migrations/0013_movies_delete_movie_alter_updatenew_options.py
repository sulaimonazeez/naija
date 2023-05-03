# Generated by Django 4.1.7 on 2023-03-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_updatenew'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=255)),
                ('feature', models.CharField(blank=True, max_length=255)),
                ('titles', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('albums', models.ImageField(upload_to='myapp/video')),
                ('file', models.FileField(upload_to='myapp/video')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.AlterModelOptions(
            name='updatenew',
            options={'ordering': ('-id',)},
        ),
    ]