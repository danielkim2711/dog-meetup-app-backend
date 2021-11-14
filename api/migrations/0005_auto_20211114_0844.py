# Generated by Django 3.2.9 on 2021-11-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_dog_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/users/'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/dogs/'),
        ),
    ]
