# Generated by Django 3.2.2 on 2021-05-10 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('destination', models.TextField()),
                ('season', models.TextField()),
                ('description', models.TextField()),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addntravel.travel')),
            ],
        ),
    ]
