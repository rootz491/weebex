# Generated by Django 3.1.3 on 2020-12-24 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('weeb', '0005_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('username', models.CharField(max_length=30)),
                ('joinedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
