from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_educationdirection_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationprocess',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationprocess',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='education/process/'),
        ),
    ]
