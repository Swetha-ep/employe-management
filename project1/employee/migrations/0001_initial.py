# Generated by Django 5.0 on 2023-12-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('department', models.CharField(choices=[('IT', 'Information Technology'), ('HR', 'Human Resources'), ('Finance', 'Finance')], max_length=30)),
            ],
        ),
    ]
