# Generated by Django 2.1.3 on 2018-11-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('horario_funcionamento', models.TextField()),
                ('idade_minima', models.IntegerField()),
            ],
        ),
    ]
