# Generated by Django 4.1.3 on 2022-12-08 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('year_of_birth', models.CharField(max_length=6)),
                ('year_of_death', models.CharField(max_length=6)),
                ('influenced_by', models.ManyToManyField(blank=True, related_name='influences', to='artists.artist')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_artists', to='artists.country')),
                ('state_of_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resident_artists', to='artists.country')),
            ],
        ),
    ]
