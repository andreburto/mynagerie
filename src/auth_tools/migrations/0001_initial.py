# Generated by Django 4.0.4 on 2022-08-29 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('credentials', models.TextField(max_length=4096)),
            ],
            options={
                'verbose_name_plural': 'Google Credentials',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GoogleSheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sheet_id', models.CharField(max_length=100)),
                ('sheet_range', models.CharField(max_length=100)),
                ('credentials', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth_tools.googlecredentials')),
            ],
            options={
                'verbose_name_plural': 'Google Sheets',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='googlecredentials',
            index=models.Index(fields=['name'], name='auth_tools__name_3ae9a7_idx'),
        ),
        migrations.AddIndex(
            model_name='googlesheets',
            index=models.Index(fields=['name'], name='auth_tools__name_4a4ef9_idx'),
        ),
        migrations.AddIndex(
            model_name='googlesheets',
            index=models.Index(fields=['sheet_id'], name='auth_tools__sheet_i_782074_idx'),
        ),
    ]
