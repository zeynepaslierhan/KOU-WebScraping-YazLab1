# Generated by Django 4.1.2 on 2022-10-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ürün',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('index', models.IntegerField()),
                ('Img', models.CharField(max_length=300)),
                ('Marka', models.CharField(blank=True, max_length=100)),
                ('BellekHızı', models.CharField(blank=True, max_length=20)),
                ('HDMI', models.CharField(blank=True, max_length=20)),
                ('EkranKartıBellekTipi', models.CharField(blank=True, max_length=20)),
                ('Renk', models.CharField(blank=True, max_length=20)),
                ('RamTipi', models.CharField(blank=True, max_length=50)),
                ('HepsiBuradaPrice', models.CharField(blank=True, max_length=300)),
                ('HepsiBuradaURL', models.CharField(blank=True, max_length=300)),
                ('HepsiBuradaRating', models.CharField(blank=True, max_length=300)),
                ('teknosaPrice', models.CharField(blank=True, max_length=300)),
                ('teknosaURL', models.CharField(blank=True, max_length=300)),
                ('teknosaRating', models.CharField(blank=True, max_length=300)),
                ('AmazonPrice', models.CharField(blank=True, max_length=300)),
                ('AmazonURL', models.CharField(blank=True, max_length=300)),
                ('AmazonRating', models.CharField(blank=True, max_length=300)),
                ('vatanBilgisayarPrice', models.CharField(blank=True, max_length=300)),
                ('vatanBilgisayarURL', models.CharField(blank=True, max_length=300)),
                ('vatanBilgisayarRating', models.CharField(blank=True, max_length=300)),
                ('cicekSepetiExtraPrice', models.CharField(blank=True, max_length=300)),
                ('cicekSepetiExtraURL', models.CharField(blank=True, max_length=300)),
                ('cicekSepetiExtraRating', models.CharField(blank=True, max_length=300)),
                ('TrendyolPrice', models.CharField(blank=True, max_length=300)),
                ('TrendyolURL', models.CharField(blank=True, max_length=300)),
                ('TrendyolRating', models.CharField(blank=True, max_length=300)),
                ('n11Price', models.CharField(blank=True, max_length=300)),
                ('n11URL', models.CharField(blank=True, max_length=300)),
                ('n11Rating', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
