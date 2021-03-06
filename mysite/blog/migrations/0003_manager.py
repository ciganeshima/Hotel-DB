# Generated by Django 2.1.3 on 2018-11-29 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=5)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='blog.Room')),
            ],
        ),
    ]
