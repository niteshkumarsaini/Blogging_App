# Generated by Django 4.2 on 2023-05-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_customuser_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(upload_to='profiles/'),
        ),
    ]
