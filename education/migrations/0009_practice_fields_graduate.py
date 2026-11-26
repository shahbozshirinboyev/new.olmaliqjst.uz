from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
        ('education', '0008_alter_assessment_options_alter_control_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practice',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='practice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='education/practice/', verbose_name='Rasm'),
        ),
        migrations.AddField(
            model_name='practice',
            name='partner',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='practices',
                to='partners.partner',
                verbose_name='Hamkor tashkilot',
            ),
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_type',
            field=models.CharField(
                blank=True,
                choices=[
                    ('ishlab_chiharish', 'Ishlab chiqarish amaliyoti'),
                    ('pedagogik', 'Pedagogik amaliyot'),
                    ('diplom_oldi', 'Diplom oldi amaliyoti'),
                ],
                max_length=30,
                verbose_name='Amaliyot turi',
            ),
        ),
        migrations.AddField(
            model_name='practice',
            name='period',
            field=models.CharField(blank=True, max_length=50, verbose_name='Davr'),
        ),
        migrations.AddField(
            model_name='practice',
            name='sort_order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Tartib'),
        ),
        migrations.AddField(
            model_name='practice',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name="Ko'rsatilsin"),
        ),
        migrations.AlterField(
            model_name='practice',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='partner_name',
            field=models.CharField(blank=True, max_length=200, verbose_name="Hamkor nomi (qo'lda)"),
        ),
        migrations.AlterModelOptions(
            name='practice',
            options={'ordering': ['sort_order', '-updated_at'], 'verbose_name': 'Amaliyot', 'verbose_name_plural': 'Amaliyotlar'},
        ),
        migrations.CreateModel(
            name='Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familiya')),
                ('middle_name', models.CharField(blank=True, max_length=100, verbose_name='Otasining ismi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='education/graduates/', verbose_name='Rasm')),
                ('graduation_year', models.PositiveSmallIntegerField(verbose_name='Bitirgan yili')),
                ('bio', models.TextField(blank=True, verbose_name='Bitiruvchi haqida')),
                ('position', models.CharField(blank=True, max_length=200, verbose_name='Hozirgi lavozimi')),
                ('workplace', models.CharField(blank=True, max_length=200, verbose_name='Ish joyi')),
                ('achievement', models.TextField(blank=True, verbose_name='Yutuqlari')),
                ('quote', models.CharField(blank=True, max_length=300, verbose_name='Maslahati')),
                ('sort_order', models.PositiveSmallIntegerField(default=0, verbose_name='Tartib')),
                ('is_active', models.BooleanField(default=True, verbose_name="Ko'rsatilsin")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('direction', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='graduates',
                    to='education.educationdirection',
                    verbose_name="Yo'nalish",
                )),
            ],
            options={
                'verbose_name': 'Bitiruvchi',
                'verbose_name_plural': 'Bitiruvchilar',
                'ordering': ['sort_order', '-graduation_year', 'last_name'],
            },
        ),
    ]
