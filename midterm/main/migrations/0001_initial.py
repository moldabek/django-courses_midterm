# Generated by Django 3.1.7 on 2021-03-20 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookJournalBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Bullet'), (2, 'Food'), (3, 'Travel'), (4, 'Sport')])),
                ('publisher', models.CharField(max_length=255)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bookjournalbase')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pages', models.IntegerField()),
                ('genres', models.CharField(max_length=255)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bookjournalbase')),
            ],
        ),
    ]
