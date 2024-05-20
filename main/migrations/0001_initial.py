# Generated by Django 3.2.5 on 2023-05-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='readings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reinfall', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Nitrogen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Phosphorus', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Potassium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ph', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
    ]
