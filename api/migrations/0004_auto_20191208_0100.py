# Generated by Django 3.0 on 2019-12-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customgroup_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]