# Generated by Django 3.1.5 on 2021-01-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BC_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='num_of_transaction',
            field=models.PositiveIntegerField(null=True, verbose_name='Num of transaction'),
        ),
    ]
