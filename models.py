# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    idadmin = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employee', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    in_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='in_project', blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    decription = models.CharField(max_length=45, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lot = models.ForeignKey('Lots', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BankAccount(models.Model):
    bank_account_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=50)
    real_balance = models.DecimalField(max_digits=15, decimal_places=2)
    account_num = models.CharField(max_length=60, blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_account'


class BankTransaction(models.Model):
    bank_account = models.ForeignKey(BankAccount, models.DO_NOTHING, blank=True, null=True)
    cheque_number = models.CharField(max_length=20, blank=True, null=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=7)
    cheque_file = models.TextField(blank=True, null=True)
    payer_type = models.CharField(max_length=13, blank=True, null=True)
    pay_method = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_transaction'


class BonCommandSt(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.ForeignKey(Articles, models.DO_NOTHING, db_column='article', blank=True, null=True)
    sous_traitant = models.ForeignKey('SousTraitant', models.DO_NOTHING, db_column='sous_traitant', blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    data_generated = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bon_command_st'


class BonLivraisionCl(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    date_delivery = models.DateField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bon_livraision_cl'


class BonLivraisonSt(models.Model):
    id = models.IntegerField(primary_key=True)
    article_bl = models.ForeignKey(Articles, models.DO_NOTHING, db_column='article_bl', blank=True, null=True)
    date_livraision = models.DateTimeField(blank=True, null=True)
    file_bon = models.TextField(blank=True, null=True)
    sous_tr = models.ForeignKey('SousTraitant', models.DO_NOTHING, db_column='sous_tr', blank=True, null=True)
    quantity_livre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bon_livraison_st'


class Caisse(models.Model):
    caisse_id = models.AutoField(primary_key=True)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)
    update_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caisse'


class CaisseTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    caisse = models.ForeignKey(Caisse, models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=6)
    designation = models.CharField(max_length=255, blank=True, null=True)
    payer_type = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caisse_transaction'


class ClientPayments(models.Model):
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=13)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_payments'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Company(models.Model):
    name = models.CharField(max_length=45)
    rc = models.CharField(db_column='RC', max_length=45)  # Field name made lowercase.
    adress = models.CharField(max_length=450)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=450)
    nif = models.CharField(db_column='NIF', max_length=45)  # Field name made lowercase.
    nis = models.CharField(db_column='NIS', max_length=45)  # Field name made lowercase.
    rib = models.CharField(db_column='RIB', max_length=45)  # Field name made lowercase.
    url_web = models.CharField(db_column='URL_web', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class Conge(models.Model):
    idconge = models.AutoField(primary_key=True)
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
    idcontrat = models.AutoField(primary_key=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING)
    contrat_type = models.CharField(max_length=45)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    salary_amount = models.CharField(max_length=45)
    status = models.CharField(max_length=8)
    job_title = models.CharField(max_length=45)
    contrat_terms = models.TextField(blank=True, null=True)
    work_location = models.CharField(max_length=255, blank=True, null=True)
    work_hours = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrat'


class Devis(models.Model):
    devis_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=12, blank=True, null=True)
    devis_date = models.DateField(blank=True, null=True)
    payment_status = models.CharField(max_length=18, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rest_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tva_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tva_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_ttc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    devis_status = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devis'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    idemployee = models.AutoField(primary_key=True)
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='iduser', blank=True, null=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    birth_date = models.DateField(blank=True, null=True)
    birth_address = models.CharField(max_length=45, blank=True, null=True)
    adress = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    gendre = models.CharField(max_length=45, blank=True, null=True)
    blood_type = models.CharField(max_length=45, blank=True, null=True)
    situation = models.CharField(max_length=45, blank=True, null=True)
    nbr_child = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    num_carte = models.IntegerField(blank=True, null=True)
    num_ss = models.IntegerField(db_column='num-ss')  # Field renamed to remove unsuitable characters.
    role = models.CharField(max_length=45)
    departement = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeePayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=13)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_payment'


class EmployeeProject(models.Model):
    article = models.OneToOneField(Articles, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    assigned_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_project'


class Fournisseur(models.Model):
    idfournisseur = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    business_type = models.CharField(max_length=10, blank=True, null=True)
    rc = models.CharField(db_column='RC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    centre_cout = models.CharField(max_length=45, blank=True, null=True)
    siege_social = models.CharField(max_length=45, blank=True, null=True)
    nis = models.CharField(db_column='NIS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nif = models.CharField(db_column='NIF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rip = models.CharField(db_column='RIP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=8, blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    bank_account_num = models.CharField(max_length=45, blank=True, null=True)
    contract_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fournisseur'


class FournisseurPayments(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING, db_column='fournisseur')
    resource = models.ForeignKey('Resources', models.DO_NOTHING)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=13)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fournisseur_payments'


class Lots(models.Model):
    idlots = models.AutoField(primary_key=True)
    num_lot = models.IntegerField(blank=True, null=True)
    capacity = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=450, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lots'


class Manager(models.Model):
    idmanager = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class OtherOutcome(models.Model):
    outcome_date = models.DateTimeField()
    outcome_name = models.CharField(max_length=45)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_outcome'


class Owner(models.Model):
    idowner = models.OneToOneField('Users', models.DO_NOTHING, db_column='idowner', primary_key=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Payrolls(models.Model):
    payroll_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    pay_date = models.DateField(blank=True, null=True)
    pay_period_start = models.DateField(blank=True, null=True)
    pay_period_end = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    total_hours_work = models.TimeField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    overtime_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    regular_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    overtime_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_status = models.CharField(max_length=7, blank=True, null=True)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payrolls'


class Pointage(models.Model):
    idpointage = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee-id')  # Field renamed to remove unsuitable characters.
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    total_hours_worked = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pointage'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rested_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectSoutraitant(models.Model):
    project_soustraitant_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Articles, models.DO_NOTHING)
    soustraitant = models.ForeignKey('SousTraitant', models.DO_NOTHING)
    bc = models.ForeignKey(BonCommandSt, models.DO_NOTHING, db_column='bc', blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    assigned_date = models.DateField()
    expected_delivery = models.DateField()
    payment_status = models.CharField(max_length=18, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_soutraitant'


class ProjectTracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    update_description = models.TextField(blank=True, null=True)
    update_date = models.DateField()
    status = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tracking'


class Resources(models.Model):
    idresources = models.AutoField(primary_key=True)
    fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING)
    lot = models.ForeignKey(Lots, models.DO_NOTHING, db_column='lot')
    name = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'


class ReviewEmployer(models.Model):
    idreview_employer = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    review_date = models.DateField(blank=True, null=True)
    rating = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_employer'


class Salary(models.Model):
    idsalary = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField()
    salary_type = models.CharField(max_length=8)
    overtime_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bunuses = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'salary'


class Secretary(models.Model):
    idsecretary = models.OneToOneField(Employee, models.DO_NOTHING, db_column='idsecretary', primary_key=True)

    class Meta:
        managed = False
        db_table = 'secretary'


class SousTrPayments(models.Model):
    sous_tr = models.ForeignKey('SousTraitant', models.DO_NOTHING)
    article = models.ForeignKey(Articles, models.DO_NOTHING)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=13)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sous_tr_payments'


class SousTraitant(models.Model):
    idsous_traitant = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
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
    idusers = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    user_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'users'
