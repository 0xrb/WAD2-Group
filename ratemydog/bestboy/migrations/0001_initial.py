# Generated by Django 2.1.7 on 2019-03-19 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(choices=[('UK', 'Unkown'), ('GS', 'Leo has no nuts'), ('DM', 'Dobermann'), ('DH', 'Dachshund')], default='Unkown', max_length=20)),
                ('score', models.FloatField(default=0)),
                ('average', models.FloatField(default=0)),
                ('picture', models.ImageField(upload_to='bestboy/dog_pics/', verbose_name='img')),
                ('votes', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('text', models.TextField(max_length=3000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestboy.Dog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
