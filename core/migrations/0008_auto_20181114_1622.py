# Generated by Django 2.1.3 on 2018-11-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181114_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(blank=True, null=True, to='atracoes.Atracao'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(blank=True, null=True, to='avaliacoes.Avaliacao'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(blank=True, null=True, to='comentarios.Comentario'),
        ),
    ]
