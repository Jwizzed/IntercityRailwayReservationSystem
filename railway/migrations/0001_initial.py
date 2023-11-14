# Generated by Django 4.2.7 on 2023-11-14 03:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('ciz_id', models.CharField(blank=True, max_length=9)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('route_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('sub_dist', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('train_type_str', models.CharField(max_length=255)),
                ('manufacture_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railway.route')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railway.seat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='seat',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='railway.train'),
        ),
        migrations.AddField(
            model_name='route',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departing_routes', to='railway.station'),
        ),
        migrations.AddField(
            model_name='route',
            name='terminal_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriving_routes', to='railway.station'),
        ),
        migrations.AddField(
            model_name='route',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railway.train'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rev_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_from_station', to='railway.station')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railway.ticket')),
                ('to_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_to_station', to='railway.station')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
