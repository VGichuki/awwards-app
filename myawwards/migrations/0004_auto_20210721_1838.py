# Generated by Django 3.2.5 on 2021-07-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0003_auto_20210721_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]