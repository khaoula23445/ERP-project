# Generated by Django 5.1.2 on 2024-10-31 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='caisse',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='caissetransaction',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='chequetransaction',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='conge',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='contrat',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='employeepayment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='employeeproject',
            options={'managed': True},
        ),
    ]
