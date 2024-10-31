# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    idadmin = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employee', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lot = models.ForeignKey('Lots', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix_estimation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix_soumission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    marche_benifit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fournisseur = models.ForeignKey('Fournisseur', models.DO_NOTHING, db_column='fournisseur', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class BankAccount(models.Model):
    bank_account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=50)
    real_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    credit_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    debit_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_account'


class Caisse(models.Model):
    caisse_id = models.AutoField(primary_key=True)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caisse'


class CaisseTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    caisse = models.ForeignKey(Caisse, models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=6)
    beneficiary = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    receipt_file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caisse_transaction'


class ChequeTransaction(models.Model):
    cheque_id = models.AutoField(primary_key=True)
    bank_account = models.ForeignKey(BankAccount, models.DO_NOTHING, blank=True, null=True)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    cheque_number = models.CharField(max_length=20, blank=True, null=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=6)
    remaining_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque_transaction'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Conge(models.Model):
    idconge = models.IntegerField(primary_key=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    conge_type = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    num_days = models.IntegerField(blank=True, null=True)
    num_days_rest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conge'


class Contrat(models.Model):
    idcontrat = models.IntegerField(primary_key=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING)
    contrat_type = models.CharField(max_length=45)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    salary_amount = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45)
    function = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrat'


class Employee(models.Model):
    idemployee = models.IntegerField(primary_key=True)
    num_ss = models.IntegerField(db_column='num-ss')  # Field renamed to remove unsuitable characters.
    type = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    birth_date = models.DateField(blank=True, null=True)
    adress = models.CharField(max_length=45)
    phone = models.IntegerField()
    email = models.CharField(max_length=45)
    gendre = models.CharField(max_length=45, blank=True, null=True)
    situation = models.CharField(max_length=45, blank=True, null=True)
    nbr_child = models.IntegerField(blank=True, null=True)
    blood_type = models.CharField(max_length=45, blank=True, null=True)
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='iduser', blank=True, null=True)
    birth_address = models.CharField(max_length=45, blank=True, null=True)
    num_carte = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeePayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=13)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bank_deduction = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    caisse = models.ForeignKey(Caisse, models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey(BankAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_payment'


class EmployeeProject(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    assigned_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_project'


class FinalInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    issue_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rest_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=14, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_invoice'


class Fournisseur(models.Model):
    idfournisseur = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    rc = models.CharField(db_column='RC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    centre_cout = models.CharField(max_length=45, blank=True, null=True)
    siege_social = models.CharField(max_length=45, blank=True, null=True)
    nis = models.CharField(db_column='NIS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nif = models.CharField(db_column='NIF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rip = models.CharField(db_column='RIP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fournisseur'


class Lots(models.Model):
    idlots = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'lots'


class Manager(models.Model):
    idmanager = models.ForeignKey(Employee, models.DO_NOTHING, db_column='idmanager', primary_key=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Owner(models.Model):
    idowner = models.ForeignKey('Users', models.DO_NOTHING, db_column='idowner', primary_key=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Payrolls(models.Model):
    payroll_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    salary = models.ForeignKey('Salary', models.DO_NOTHING, blank=True, null=True)
    pay_date = models.DateField(blank=True, null=True)
    pay_period_start = models.DateField(blank=True, null=True)
    pay_period_end = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payrolls'


class Pointage(models.Model):
    idpointage = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    employee_id = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee-id')  # Field renamed to remove unsuitable characters.
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pointage'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectSoutraitant(models.Model):
    project_soustraitant_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    soustraitant = models.ForeignKey('SousTraitant', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_soutraitant'


class ProjectTracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    update_description = models.TextField(blank=True, null=True)
    update_date = models.DateField()
    status = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tracking'


class ReviewEmployer(models.Model):
    idreview_employer = models.ForeignKey(Employee, models.DO_NOTHING, db_column='idreview_employer', primary_key=True)
    employee_id = models.IntegerField(blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    rating = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_employer'


class Salary(models.Model):
    idsalary = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    base_salary = models.CharField(max_length=45, blank=True, null=True)
    net_salary = models.CharField(max_length=45, blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary'


class Secretary(models.Model):
    idsecretary = models.ForeignKey(Employee, models.DO_NOTHING, db_column='idsecretary', primary_key=True)

    class Meta:
        managed = False
        db_table = 'secretary'


class SousTraitant(models.Model):
    idsous_traitant = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    rip = models.CharField(db_column='RIP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nif = models.CharField(db_column='NIF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nis = models.CharField(db_column='NIS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rc = models.CharField(db_column='RC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    centre_cout = models.CharField(max_length=100, blank=True, null=True)
    siege_social = models.CharField(max_length=100, blank=True, null=True)
    num_ref = models.CharField(max_length=100, blank=True, null=True)
    num_contrat = models.CharField(max_length=100, blank=True, null=True)
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sous_traitant'


class Users(models.Model):
    idusers = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    user_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'users'
