# Generated by Django 5.0.7 on 2024-07-18 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_remove_workoutlog_workout_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpackage',
            old_name='user',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='workoutlog',
            old_name='user',
            new_name='customer',
        ),
    ]
