# Generated by Django 2.1.7 on 2019-03-02 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestboy', '0004_auto_20190302_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bestboy.Test_User'),
        ),
    ]