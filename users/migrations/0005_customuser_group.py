# Generated by Django 5.0.7 on 2024-07-18 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0004_remove_customuser_age_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]
