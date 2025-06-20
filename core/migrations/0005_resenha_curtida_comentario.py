# Generated by Django 5.2.1 on 2025-06-13 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_email_alter_user_passage_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curtida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curtida', models.BooleanField()),
                ('resenha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Curtida_resenha', to='core.resenha')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=250, null=True)),
                ('resenha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Comentario_resenha', to='core.resenha')),
            ],
        ),
    ]
