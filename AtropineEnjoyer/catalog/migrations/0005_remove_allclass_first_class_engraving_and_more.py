# Generated by Django 4.2.11 on 2024-04-12 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_allclass_genre_name_case_insensitive_unique_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allclass',
            name='first_class_engraving',
        ),
        migrations.RemoveField(
            model_name='allclass',
            name='second_class_engraving',
        ),
        migrations.AddField(
            model_name='classengraving',
            name='associated_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.allclass'),
        ),
    ]
