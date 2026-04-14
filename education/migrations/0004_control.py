from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_educationprocess_created_at_educationprocess_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Nazorat',
                'verbose_name_plural': 'Nazorat',
            },
        ),
    ]
