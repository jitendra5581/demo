# Generated by Django 2.0.5 on 2019-09-25 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patientapp', '0005_delete_dietdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooditem', models.CharField(max_length=100)),
                ('foodtimes', models.CharField(max_length=100)),
                ('foodtakenday', models.CharField(max_length=100)),
                ('takenduration', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
