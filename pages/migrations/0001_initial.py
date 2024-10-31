# Generated by Django 5.1.2 on 2024-10-31 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('idadmin', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('prix_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('prix_estimation', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('prix_soumission', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('marche_benifit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('bank_account_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=50)),
                ('real_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('credit_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('debit_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'bank_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Caisse',
            fields=[
                ('caisse_id', models.AutoField(primary_key=True, serialize=False)),
                ('current_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('last_update', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'caisse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CaisseTransaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('transaction_type', models.CharField(max_length=6)),
                ('beneficiary', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('receipt_file', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'caisse_transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChequeTransaction',
            fields=[
                ('cheque_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_number', models.CharField(blank=True, max_length=20, null=True)),
                ('transaction_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('transaction_type', models.CharField(max_length=6)),
                ('remaining_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'cheque_transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('idconge', models.IntegerField(primary_key=True, serialize=False)),
                ('conge_type', models.CharField(blank=True, max_length=45, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('num_days', models.IntegerField(blank=True, null=True)),
                ('num_days_rest', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'conge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('idcontrat', models.IntegerField(primary_key=True, serialize=False)),
                ('contrat_type', models.CharField(max_length=45)),
                ('start_date', models.CharField(blank=True, max_length=45, null=True)),
                ('end_date', models.CharField(blank=True, max_length=45, null=True)),
                ('salary_amount', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(max_length=45)),
                ('function', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'contrat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('idemployee', models.IntegerField(primary_key=True, serialize=False)),
                ('num_ss', models.IntegerField(db_column='num-ss')),
                ('type', models.CharField(max_length=45)),
                ('firstname', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('adress', models.CharField(max_length=45)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=45)),
                ('gendre', models.CharField(blank=True, max_length=45, null=True)),
                ('situation', models.CharField(blank=True, max_length=45, null=True)),
                ('nbr_child', models.IntegerField(blank=True, null=True)),
                ('blood_type', models.CharField(blank=True, max_length=45, null=True)),
                ('birth_address', models.CharField(blank=True, max_length=45, null=True)),
                ('num_carte', models.IntegerField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeePayment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField()),
                ('payment_method', models.CharField(max_length=13)),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bank_deduction', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('net_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'employee_payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('assigned_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalInvoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rest_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=14, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'final_invoice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('idfournisseur', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=45, null=True)),
                ('lastname', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('rc', models.CharField(blank=True, db_column='RC', max_length=45, null=True)),
                ('centre_cout', models.CharField(blank=True, max_length=45, null=True)),
                ('siege_social', models.CharField(blank=True, max_length=45, null=True)),
                ('nis', models.CharField(blank=True, db_column='NIS', max_length=45, null=True)),
                ('nif', models.CharField(blank=True, db_column='NIF', max_length=45, null=True)),
                ('rip', models.CharField(blank=True, db_column='RIP', max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('file', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fournisseur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lots',
            fields=[
                ('idlots', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'lots',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('idusers', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('user_type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payrolls',
            fields=[
                ('payroll_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_date', models.DateField(blank=True, null=True)),
                ('pay_period_start', models.DateField(blank=True, null=True)),
                ('pay_period_end', models.DateField(blank=True, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'payrolls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('idpointage', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('check_in_time', models.TimeField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'pointage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=11, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectSoutraitant',
            fields=[
                ('project_soustraitant_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'project_soutraitant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTracking',
            fields=[
                ('tracking_id', models.AutoField(primary_key=True, serialize=False)),
                ('update_description', models.TextField(blank=True, null=True)),
                ('update_date', models.DateField()),
                ('status', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'project_tracking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('idsalary', models.IntegerField(primary_key=True, serialize=False)),
                ('base_salary', models.CharField(blank=True, max_length=45, null=True)),
                ('net_salary', models.CharField(blank=True, max_length=45, null=True)),
                ('date_issued', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'salary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SousTraitant',
            fields=[
                ('idsous_traitant', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('rip', models.CharField(blank=True, db_column='RIP', max_length=100, null=True)),
                ('nif', models.CharField(blank=True, db_column='NIF', max_length=100, null=True)),
                ('nis', models.CharField(blank=True, db_column='NIS', max_length=100, null=True)),
                ('rc', models.CharField(blank=True, db_column='RC', max_length=100, null=True)),
                ('centre_cout', models.CharField(blank=True, max_length=100, null=True)),
                ('siege_social', models.CharField(blank=True, max_length=100, null=True)),
                ('num_ref', models.CharField(blank=True, max_length=100, null=True)),
                ('num_contrat', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sous_traitant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('idmanager', models.ForeignKey(db_column='idmanager', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.employee')),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewEmployer',
            fields=[
                ('idreview_employer', models.ForeignKey(db_column='idreview_employer', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.employee')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('review_date', models.DateField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, max_length=45, null=True)),
                ('comment', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'review_employer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('idsecretary', models.ForeignKey(db_column='idsecretary', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.employee')),
            ],
            options={
                'db_table': 'secretary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('idowner', models.ForeignKey(db_column='idowner', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.users')),
            ],
            options={
                'db_table': 'owner',
                'managed': False,
            },
        ),
    ]
