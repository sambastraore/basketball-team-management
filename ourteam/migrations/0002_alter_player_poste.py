# Generated by Django 4.1.7 on 2023-07-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='poste',
            field=models.CharField(choices=[('PG', 'Meneur'), ('SG', 'Arrière'), ('SF', 'Ailier'), ('PF', 'Ailier fort'), ('C', 'Pivot')], max_length=2),
        ),
    ]
