# Generated by Django 5.0.3 on 2024-03-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userprofile_referral_code_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='referral_code_used',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]