# Generated by Django 5.1.5 on 2025-05-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0004_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='menu_images/'),
        ),
    ]
