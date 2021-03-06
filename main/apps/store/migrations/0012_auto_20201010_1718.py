# Generated by Django 3.0.8 on 2020-10-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201009_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Ayirboshlash', 'Ayirboshlash'), ('Bepul', 'Bepul'), ('Narx', 'Narx')], max_length=100, null=True)),
                ('valute', models.CharField(choices=[('sum', 'sum'), ('y.e.', 'y.e.')], max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('model', models.CharField(choices=[('Tissot', 'Tissot'), ('Adriatica', 'Adriatica'), ('Aigner', 'Aigner'), ('Alfex', 'Alfex'), ('AndyWatch', 'AndyWatch'), ('Anne Klein', 'Anne Klein'), ('Appella', 'Appella'), ('Appetime', 'Appetime'), ('Aristo', 'Aristo'), ('Armand Basi', 'Armand Basi'), ('Armand Nicolet', 'Armand Nicolet'), ('Armani', 'Armani'), ('Atlantic', 'Atlantic'), ('Auguste Reymond', 'Auguste Reymond'), ('Axcent', 'Axcent'), ('Balmain', 'Balmain'), ('Baume', 'Baume'), ('Benetton', 'Benetton')], max_length=100, null=True)),
                ('condition', models.CharField(choices=[('Ishlatilgan', 'Ishlatilgan'), ('Yangi', 'Yangi')], max_length=100, null=True)),
                ('seller', models.CharField(choices=[('Jismoniy shaxs', 'Jismoniy shaxs'), ('Yuridik shaxs', 'Yuridik shaxs')], max_length=100, null=True)),
                ('parent_product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.ProductParent')),
            ],
        ),
        migrations.DeleteModel(
            name='WorkProgrammer',
        ),
    ]
