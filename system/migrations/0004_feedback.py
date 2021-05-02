# Generated by Django 3.0.6 on 2021-05-02 18:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_employee_works_at_showroom'),
        ('system', '0003_auto_20210502_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback_Date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('message', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Customer')),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.SaleOrder')),
            ],
        ),
    ]
