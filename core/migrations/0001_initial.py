# Generated by Django 2.2.2 on 2019-07-01 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your habit here', max_length=300)),
                ('description', models.TextField(help_text='Enter the decription of your habit here')),
                ('target', models.IntegerField(help_text='Enter a target number for your habit')),
                ('observers', models.ManyToManyField(to='core.Observer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField(help_text='Enter the day number for your habit')),
                ('date', models.DateField(help_text='Enter the date')),
                ('description', models.TextField(help_text='Enter the description of your progress here')),
                ('progress', models.IntegerField(help_text='Enter your progress here')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Enter your comment here')),
                ('daily_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DailyRecord')),
                ('observer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Observer')),
            ],
        ),
    ]
