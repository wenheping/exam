# Generated by Django 3.1.3 on 2020-11-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attrib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_id', models.IntegerField(default=0)),
                ('w_shijuan_lei', models.CharField(max_length=20)),
                ('w_shiti_lei', models.CharField(max_length=20)),
                ('w_quyu', models.CharField(max_length=20)),
                ('w_nian', models.CharField(max_length=10)),
                ('w_nandu', models.CharField(max_length=10)),
                ('w_zhiliang', models.CharField(max_length=10)),
                ('w_zhishidian', models.CharField(max_length=10)),
                ('w_guanjianci', models.CharField(max_length=10)),
            ],
        ),
    ]
