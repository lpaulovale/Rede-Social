# Generated by Django 3.1.8 on 2023-01-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20230107_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='lastname',
        ),
        migrations.AddField(
            model_name='usuario',
            name='aviso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='descricao1',
            field=models.CharField(default='Água', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='descricao2',
            field=models.CharField(default='Alimentação', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='descricao3',
            field=models.CharField(default='Medicação', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='descricao4',
            field=models.CharField(default='Munição', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='infectado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='latitude',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='usuario',
            name='longitude',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pontos1',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pontos2',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pontos3',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pontos4',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usuario',
            name='quantidade1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='quantidade2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='quantidade3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='quantidade4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(default='', max_length=20),
        ),
    ]
