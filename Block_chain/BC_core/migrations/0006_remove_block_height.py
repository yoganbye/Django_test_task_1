# Generated by Django 3.1.5 on 2021-01-16 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BC_core', '0005_block_hash_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='height',
        ),
    ]