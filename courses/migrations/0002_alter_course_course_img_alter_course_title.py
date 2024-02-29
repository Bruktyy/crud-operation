# Generated by Django 4.2.4 on 2023-08-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_img',
            field=models.ImageField(default='default.jpg', upload_to='course_images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
