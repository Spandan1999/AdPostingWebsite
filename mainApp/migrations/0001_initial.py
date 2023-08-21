# Generated by Django 4.2.4 on 2023-08-17 17:54

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
            name='AdPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_type', models.CharField(choices=[('rent', 'Rent Ads'), ('sell', 'Sell Ads'), ('job', 'Job Ads'), ('commercial', 'Commercial Ads')], max_length=20)),
                ('ad_title', models.CharField(max_length=100)),
                ('ad_description', models.TextField()),
                ('contact_info', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
