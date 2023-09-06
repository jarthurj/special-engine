# Generated by Django 4.2.3 on 2023-09-06 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('scryfall_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flavor_text', models.CharField(max_length=255)),
                ('collector_number', models.CharField(max_length=10)),
                ('oracle_text', models.CharField(max_length=200)),
                ('image_small', models.URLField(null=True)),
                ('image_normal', models.URLField(null=True)),
                ('image_large', models.URLField(null=True)),
                ('type_line', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('set_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cmc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmc', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Digital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digital', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ManaCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mana_cost', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Toughness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toughness', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Legality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legality', models.CharField(max_length=20)),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legalities', to='card_search.gametype')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20)),
                ('cards', models.ManyToManyField(related_name='keywords', to='card_search.card')),
            ],
        ),
        migrations.CreateModel(
            name='ColorIdentity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_identity', models.CharField(max_length=3)),
                ('cards', models.ManyToManyField(related_name='color_identities', to='card_search.card')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=3)),
                ('cards', models.ManyToManyField(related_name='colors', to='card_search.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.cardset'),
        ),
        migrations.AddField(
            model_name='card',
            name='cmc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.cmc'),
        ),
        migrations.AddField(
            model_name='card',
            name='digital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.digital'),
        ),
        migrations.AddField(
            model_name='card',
            name='layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.layout'),
        ),
        migrations.AddField(
            model_name='card',
            name='legality',
            field=models.ManyToManyField(related_name='cards', to='card_search.legality'),
        ),
        migrations.AddField(
            model_name='card',
            name='mana_cost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.manacost'),
        ),
        migrations.AddField(
            model_name='card',
            name='power',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.power'),
        ),
        migrations.AddField(
            model_name='card',
            name='rarity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.rarity'),
        ),
        migrations.AddField(
            model_name='card',
            name='reserved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.reserved'),
        ),
        migrations.AddField(
            model_name='card',
            name='toughness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.toughness'),
        ),
    ]
