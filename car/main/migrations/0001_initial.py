# Generated by Django 5.0.7 on 2024-07-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=232)),
                ('text_problem', models.TextField()),
                ('date_problem', models.DateField()),
                ('contact_info', models.CharField(max_length=232)),
            ],
        ),
    ]
