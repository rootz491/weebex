# Generated by Django 3.1.4 on 2020-12-24 08:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('weeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for each post', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(help_text='try to upload a square picture.', upload_to='img'),
        ),
    ]
