# Generated by Django 4.1.5 on 2023-01-18 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Artist_Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_collective_ink_serverapi.artist')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_collective_ink_serverapi.style')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_collective_ink_serverapi.shop'),
        ),
        migrations.AddField(
            model_name='artist',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_collective_ink_serverapi.style'),
        ),
    ]
