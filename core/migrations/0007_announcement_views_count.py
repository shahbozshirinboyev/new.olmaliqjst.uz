from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_announcement_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
