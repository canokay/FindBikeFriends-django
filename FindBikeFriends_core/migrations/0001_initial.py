# Generated by Django 2.0.9 on 2019-04-01 10:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Reklam Başlığı')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratılma Tarihi')),
                ('description', models.TextField(max_length=1000, verbose_name='Açıklama')),
                ('start_date', models.DateTimeField(verbose_name='Başlangıç Tarihi')),
                ('end_date', models.DateTimeField(verbose_name='Bitiş Tarihi')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Reklam Ücret')),
                ('approved', models.BooleanField(verbose_name='Onaylandı')),
                ('thumbnail', models.ImageField(upload_to='images/advertisement/', verbose_name='Reklam Thumbnail')),
            ],
            options={
                'verbose_name': 'Reklam',
                'verbose_name_plural': 'Reklamlar',
            },
        ),
        migrations.CreateModel(
            name='AdvertisementImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/advertisement/', verbose_name='İsim')),
                ('advertisement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FindBikeFriends_core.Advertisement', verbose_name='Reklam')),
            ],
            options={
                'verbose_name': 'Reklam Resmi',
                'verbose_name_plural': 'Reklam Resimleri',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('first_messsage', models.CharField(max_length=500, verbose_name='İlk Mesaj')),
            ],
            options={
                'verbose_name': 'Sohbet',
                'verbose_name_plural': 'Sohbetler',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='İsim')),
                ('number', models.IntegerField(unique=True, verbose_name='İl Kodu')),
            ],
            options={
                'verbose_name': 'Şehir',
                'verbose_name_plural': 'Şehirler',
                'ordering': ('-number',),
            },
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Adres', max_length=255, verbose_name='İsim')),
                ('open_address', models.TextField(max_length=100, verbose_name='Açık Adres')),
                ('short_address', models.TextField(max_length=70, verbose_name='Kısa Adres')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Posta Kodu')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='X Koordinatı')),
                ('long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Y Koordinatı')),
            ],
            options={
                'verbose_name': 'Adres',
                'verbose_name_plural': 'Adresler',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='CompanyFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='İsim')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Reklamveren Özelliği',
                'verbose_name_plural': 'Reklamveren Özellikleri',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Etkinlik Adı')),
                ('description', models.TextField(max_length=1000, verbose_name='Açıklama')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('start_date', models.DateTimeField(verbose_name='Etkinlik Tarihi')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Etkinlik X Koordinatı')),
                ('long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Etkinlik Y Koordinatı')),
            ],
            options={
                'verbose_name': 'Etkinlik',
                'verbose_name_plural': 'Etkinlikler',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Etkinlik Tagi',
                'verbose_name_plural': 'Etkinlik Tagleri',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Takipçi',
                'verbose_name_plural': 'Takipçiler',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_message', models.CharField(max_length=500, verbose_name='Gönderilecek Mesajı')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_chat', to='FindBikeFriends_core.Chat', verbose_name='Sohbet')),
            ],
            options={
                'verbose_name': 'Sohbet Konuşması',
                'verbose_name_plural': 'Sohbet Konuşmaları',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_status', models.CharField(choices=[('User', 'Kullanici'), ('Company', 'Sirket')], max_length=15, verbose_name='Kullanıcı Durumu')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/user/profile/', verbose_name='Profil Fotoğrafı')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'verbose_name_plural': 'Tüm Kullanıcılar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identity_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='TC No')),
                ('executive_namesurname', models.CharField(blank=True, max_length=250, null=True, verbose_name='Yetkili Adı Soyadı')),
                ('executive_identity_number', models.CharField(blank=True, max_length=250, null=True, verbose_name='Yetkili TC No')),
                ('executive_email', models.CharField(blank=True, max_length=250, null=True, verbose_name='Yetkili Email')),
                ('executive_phone', models.CharField(blank=True, max_length=250, null=True, verbose_name='Yetkili Telefon Numarası')),
                ('mersis_no', models.CharField(blank=True, max_length=250, null=True, verbose_name='Mersis Numarası')),
                ('kep_address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Kep Adresi')),
                ('tax_office', models.CharField(blank=True, max_length=250, null=True, verbose_name='Vergi Dairesi')),
                ('tax_number', models.CharField(blank=True, max_length=250, null=True, verbose_name='Vergi No')),
                ('legal_company_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Yasal Şirket Ünvanı')),
                ('iban', models.CharField(blank=True, max_length=250, null=True, verbose_name='IBAN')),
                ('link_facebook', models.CharField(blank=True, max_length=250, null=True, verbose_name='Facebook Linki')),
                ('link_instagram', models.CharField(blank=True, max_length=250, null=True, verbose_name='Instagram Linki')),
                ('link_twitter', models.CharField(blank=True, max_length=250, null=True, verbose_name='Twitter Linki')),
                ('link_web', models.CharField(blank=True, max_length=250, null=True, verbose_name='Website Linki')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FindBikeFriends_core.CompanyAddress', verbose_name='Adres')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FindBikeFriends_core.City', verbose_name='Şehir')),
                ('features', models.ManyToManyField(blank=True, to='FindBikeFriends_core.CompanyFeature', verbose_name='Reklamveren Şirket Özellikleri')),
            ],
            options={
                'verbose_name': 'Reklamveren',
                'verbose_name_plural': 'Reklamverenler',
            },
            bases=('FindBikeFriends_core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='message',
            name='sent_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_user', to=settings.AUTH_USER_MODEL, verbose_name='Gönderen Kişi'),
        ),
        migrations.AddField(
            model_name='followers',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followers',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Misafirler'),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kişi'),
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FindBikeFriends_core.EventTag', verbose_name='Etkinlik Tagi'),
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_owner', to=settings.AUTH_USER_MODEL, verbose_name='Gönderen Kişi'),
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_sent_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user', to=settings.AUTH_USER_MODEL, verbose_name='Gönderilen Kişi'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisement_owner', to='FindBikeFriends_core.Company', verbose_name='Reklamveren Firma'),
        ),
    ]
