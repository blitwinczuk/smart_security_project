# Generated by Django 5.2 on 2025-05-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotionAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_id', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Unresolved', max_length=20)),
            ],
        ),
    ]
