# Generated by Django 5.0.3 on 2024-03-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_scientifique', models.CharField(max_length=255)),
                ('nom_vernaculaire', models.CharField(max_length=255)),
                ('famille_botanique', models.CharField(max_length=255)),
                ('description_botanique', models.TextField()),
                ('cycle_de_vie', models.CharField(max_length=255)),
                ('periode_de_floraison', models.CharField(max_length=255)),
                ('apparence_des_fleurs', models.CharField(max_length=255)),
                ('duree_de_la_floraison', models.CharField(max_length=255)),
                ('habitat_et_distribution', models.TextField()),
                ('exposition_au_soleil', models.CharField(max_length=255)),
                ('type_de_sol', models.CharField(max_length=255)),
                ('besoins_en_eau', models.CharField(max_length=255)),
                ('plages_de_temperature', models.CharField(max_length=255)),
                ('soins_et_culture', models.TextField()),
                ('utilisations', models.TextField()),
                ('precautions', models.TextField()),
                ('periode_de_fructification', models.CharField(max_length=255)),
                ('mois_de_debut_de_fructification', models.IntegerField()),
                ('description_des_fruits', models.TextField()),
                ('duree_de_la_fructification', models.CharField(max_length=255)),
                ('utilisations_des_fruits', models.TextField()),
            ],
        ),
    ]
