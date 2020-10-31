# Generated by Django 2.2.10 on 2020-10-31 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('readlink', models.CharField(max_length=500)),
                ('copies', models.IntegerField()),
                ('bookid', models.CharField(max_length=100)),
                ('thumbnail', models.URLField(blank=True, null=True)),
            ],
        ),
    ]