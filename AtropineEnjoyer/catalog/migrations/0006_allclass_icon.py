# Generated by Django 4.2.11 on 2024-04-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_allclass_first_class_engraving_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allclass',
            name='icon',
            field=models.ImageField(default='', upload_to='icons'),
        ),
    ]
