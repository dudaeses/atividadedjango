# Generated by Django 4.1.7 on 2023-12-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicasite', '0004_alter_banner_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='imagem',
            field=models.ImageField(upload_to='site/img/logo_and_text_color.svg'),
        ),
    ]