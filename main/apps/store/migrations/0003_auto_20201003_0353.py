# Generated by Django 3.0.8 on 2020-10-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201003_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='producthouse',
            name='payment_method',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producthouse',
            name='condition',
            field=models.CharField(choices=[('Mualliflik loyihasi', 'Mualliflik loyihasi'), ('Evrotaʼmir', 'Evrotaʼmir'), ('Oʻrtacha', 'Oʻrtacha'), ('Taʼmir talab', 'Taʼmir talab'), ('Qora suvoq', 'Qora suvoq'), ('Tozalashdan avvalgi pardoz', 'Tozalashdan avvalgi pardoz'), ('Buziladigan', 'Buziladigan')], max_length=100, null=True),
        ),
    ]
