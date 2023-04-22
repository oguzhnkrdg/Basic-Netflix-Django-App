# Generated by Django 4.2 on 2023-04-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dizi',
            name='aciklama',
        ),
        migrations.RemoveField(
            model_name='dizi',
            name='baslik',
        ),
        migrations.RemoveField(
            model_name='dizi',
            name='bolum_sayisi',
        ),
        migrations.RemoveField(
            model_name='dizi',
            name='oyuncular',
        ),
        migrations.RemoveField(
            model_name='dizi',
            name='sezon_sayisi',
        ),
        migrations.RemoveField(
            model_name='dizi',
            name='yonetmen',
        ),
        migrations.RemoveField(
            model_name='film',
            name='aciklama',
        ),
        migrations.RemoveField(
            model_name='film',
            name='baslik',
        ),
        migrations.RemoveField(
            model_name='film',
            name='oyuncular',
        ),
        migrations.RemoveField(
            model_name='film',
            name='yonetmen',
        ),
        migrations.AddField(
            model_name='dizi',
            name='isim',
            field=models.CharField(default='bos', max_length=100),
        ),
        migrations.AddField(
            model_name='dizi',
            name='resim_yolu',
            field=models.ImageField(default='bos', upload_to='diziler/'),
        ),
        migrations.AddField(
            model_name='dizi',
            name='tur',
            field=models.CharField(default='bos', max_length=100),
        ),
        migrations.AddField(
            model_name='film',
            name='isim',
            field=models.CharField(default='bos', max_length=100),
        ),
        migrations.AddField(
            model_name='film',
            name='resim_yolu',
            field=models.ImageField(default='bos', upload_to='filmler/'),
        ),
        migrations.AddField(
            model_name='film',
            name='tur',
            field=models.CharField(default='bos', max_length=100),
        ),
        migrations.DeleteModel(
            name='Oyuncu',
        ),
    ]
