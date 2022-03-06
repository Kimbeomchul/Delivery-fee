# Generated by Django 3.2.7 on 2022-03-06 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parties', '0004_remove_party_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='participants',
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('party', models.ForeignKey(help_text='참가한 파티', on_delete=django.db.models.deletion.CASCADE, to='parties.party')),
                ('user', models.OneToOneField(help_text='참가한 유저', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
