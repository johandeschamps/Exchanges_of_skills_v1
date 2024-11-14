# Generated by Django 3.2.5 on 2024-11-14 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('required_competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='required_for_slots', to='polls.skill')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('help_slots', models.ManyToManyField(related_name='helping_users', to='polls.Slot')),
                ('search_slots', models.ManyToManyField(related_name='searching_users', to='polls.Slot')),
                ('skills', models.ManyToManyField(related_name='users_with_skill', to='polls.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='user_offering_help',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offered_help_slots', to='polls.user'),
        ),
        migrations.AddField(
            model_name='slot',
            name='user_requesting_help',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_help_slots', to='polls.user'),
        ),
    ]