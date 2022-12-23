# Generated by Django 4.1.4 on 2022-12-23 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_year_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='national_artists', to='artists.country'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='state_of_residence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resident_artists', to='artists.country'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='artists.artist'),
        ),
    ]
