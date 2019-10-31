# Generated by Django 2.1.3 on 2018-12-01 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('book_room_type', models.CharField(max_length=50)),
                ('book_room_places', models.CharField(max_length=10)),
                ('arrival_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tenure', models.CharField(max_length=20)),
            ],
        ),
    ]