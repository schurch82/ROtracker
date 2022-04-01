# Generated by Django 3.1.1 on 2021-03-23 15:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RO_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ro',
            options={'ordering': ['-completed_date']},
        ),
        migrations.AddField(
            model_name='ro',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ro',
            name='RO_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='ro',
            name='completed_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 23, 15, 57, 35, 428774, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ro',
            name='pay_cycle',
            field=models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JULY', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ro',
            name='work_performed',
            field=models.CharField(max_length=200),
        ),
    ]
