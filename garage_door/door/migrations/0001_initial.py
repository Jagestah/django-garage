# Generated by Django 2.1 on 2018-08-26 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_log', models.CharField(max_length=200)),
                ('log_timestamp', models.DateTimeField(verbose_name='Logged at')),
            ],
        ),
    ]
