# Generated by Django 2.0.2 on 2018-02-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0002_auto_20180225_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='fishState',
            field=models.CharField(choices=[('NEW', 'New'), ('PROCESSING', 'Processing'), ('COMPLETED', 'Completed')], default='NEW', max_length=256),
        ),
    ]
