from django.db import models

from django.db.models import Model,ForeignKey,CharField,DateTimeField,FloatField,TextField,ManyToManyField,DecimalField,IntegerField,BooleanField,ImageField
from django.contrib.auth.models import AbstractUser

USERSTATUS=(
    ('User','Kullanici'),
    ('Company','Sirket'),
)

class User(AbstractUser):
    user_status = CharField(max_length=15, verbose_name="Kullanıcı Durumu",choices=USERSTATUS)
    profile_photo = ImageField(verbose_name='Profil Fotoğrafı', upload_to='images/user/profile/', blank=True, null=True)
    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'


class Followers(Model):
    follower = ForeignKey('FindBikeFriends_core.User', null=False, related_name='destination', on_delete=models.CASCADE)
    following = ForeignKey('FindBikeFriends_core.User', null=False, related_name='source', on_delete=models.CASCADE)
    created_at = DateTimeField(auto_now_add=True, editable=False, blank=True, null=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Takipçi'
        verbose_name_plural = 'Takipçiler'


class EventTag(Model):
    tag = TextField(verbose_name='Tag')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Etkinlik Tagi'
        verbose_name_plural = 'Etkinlik Tagleri'

    def __str__(self):
        return self.tag


class Event(Model):
    name = CharField(max_length=255, verbose_name='Etkinlik Adı')
    description = TextField(max_length=1000, verbose_name='Açıklama')
    created_at = DateTimeField(auto_now_add=True, editable=False, blank=True, null=False,verbose_name='Oluşturma Tarihi')
    start_date = DateTimeField(verbose_name='Etkinlik Tarihi')
    tag = ForeignKey('FindBikeFriends_core.EventTag', blank=True, null=True, verbose_name='Etkinlik Tagi', on_delete=models.CASCADE)
    owner = ForeignKey('FindBikeFriends_core.User', related_name='owner', verbose_name='Oluşturan Kişi', on_delete=models.CASCADE)
    lat = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Etkinlik X Koordinatı')
    long = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Etkinlik Y Koordinatı')
    guests = ManyToManyField('FindBikeFriends_core.User', blank=True, verbose_name='Misafirler')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Etkinlik'
        verbose_name_plural = 'Etkinlikler'

    def __str__(self):
        return self.name



class City(Model):
    name = CharField(max_length=255, verbose_name='İsim')
    number = IntegerField(verbose_name='İl Kodu', unique=True)

    class Meta:
        ordering = ('-number',)
        verbose_name = 'Şehir'
        verbose_name_plural = 'Şehirler'

    def __str__(self):
        return self.name


class CompanyAddress(Model):
    name = CharField(max_length=255, verbose_name='İsim', default='Adres', blank=True)
    open_address = TextField(max_length=100, verbose_name='Açık Adres')
    short_address = TextField(max_length=70, verbose_name='Kısa Adres')
    postal_code = CharField(max_length=10, null=True, blank=True, verbose_name='Posta Kodu')
    lat = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='X Koordinatı')
    long = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Y Koordinatı')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Adres'
        verbose_name_plural = 'Adresler'

    def __str__(self):
        return self.name



class CompanyFeature(Model):
    name = CharField(max_length=255, verbose_name='İsim')
    description = TextField(max_length=1000, verbose_name='Açıklama', blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Reklamveren Özelliği'
        verbose_name_plural = 'Reklamveren Özellikleri'

    def __str__(self):
        return self.name



class Company(User):
    city = ForeignKey('FindBikeFriends_core.City', blank=True, null=True, verbose_name='Şehir', on_delete=models.CASCADE)
    address = ForeignKey('FindBikeFriends_core.CompanyAddress', blank=True, null=True, verbose_name='Adres', on_delete=models.CASCADE)
    identity_number = CharField(max_length=11, null=True, blank=True, verbose_name='TC No')
    executive_namesurname = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Adı Soyadı')
    executive_identity_number = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili TC No')
    executive_email = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Email')
    executive_phone = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Telefon Numarası')
    mersis_no = CharField(max_length=250, null=True, blank=True, verbose_name='Mersis Numarası')
    kep_address = CharField(max_length=250, null=True, blank=True, verbose_name='Kep Adresi')
    tax_office = CharField(max_length=250, null=True, blank=True, verbose_name='Vergi Dairesi')
    tax_number = CharField(max_length=250, null=True, blank=True, verbose_name='Vergi No')
    legal_company_title = CharField(max_length=250, null=True, blank=True, verbose_name='Yasal Şirket Ünvanı')
    iban = CharField(max_length=250, null=True, blank=True, verbose_name='IBAN')
    link_facebook = CharField(max_length=250, null=True, blank=True, verbose_name='Facebook Linki')
    link_instagram = CharField(max_length=250, null=True, blank=True, verbose_name='Instagram Linki')
    link_twitter = CharField(max_length=250, null=True, blank=True, verbose_name='Twitter Linki')
    link_web = CharField(max_length=250, null=True, blank=True, verbose_name='Website Linki')
    features = ManyToManyField('FindBikeFriends_core.CompanyFeature', verbose_name='Reklamveren Şirket Özellikleri', blank=True)

    class Meta:
        verbose_name = 'Reklamveren'
        verbose_name_plural = 'Reklamverenler'



class Advertisement(Model):
    name = CharField(max_length=255, verbose_name='Reklam Başlığı')
    created = DateTimeField(auto_now_add=True, editable=False, verbose_name='Yaratılma Tarihi')
    description = TextField(max_length=1000, verbose_name='Açıklama')
    start_date = DateTimeField(verbose_name='Başlangıç Tarihi')
    end_date = DateTimeField(verbose_name='Bitiş Tarihi')
    price = FloatField(verbose_name='Reklam Ücret', blank=True, null=True)
    approved = BooleanField(verbose_name='Onaylandı')
    owner = ForeignKey('FindBikeFriends_core.Company', related_name='advertisement_owner', verbose_name='Reklamveren Firma', on_delete=models.CASCADE)
    thumbnail = ImageField(verbose_name='Reklam Thumbnail', upload_to='images/advertisement/')


    class Meta:
        verbose_name = 'Reklam'
        verbose_name_plural = 'Reklamlar'


class AdvertisementImage(Model):
    image = ImageField(verbose_name='İsim', upload_to='images/advertisement/')
    advertisement = ForeignKey('FindBikeFriends_core.Advertisement', verbose_name='Reklam', null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Reklam Resmi'
        verbose_name_plural = 'Reklam Resimleri'

    def __str__(self):
        return self.image.name


class Chat(Model):
    chat_owner = ForeignKey("FindBikeFriends_core.User",null=False, related_name='chat_owner', on_delete=models.CASCADE, verbose_name="Gönderen Kişi")
    chat_sent_user = ForeignKey("FindBikeFriends_core.User",null=False,related_name='chat_user', on_delete=models.CASCADE, verbose_name="Gönderilen Kişi")
    created_at = DateTimeField(auto_now_add=True, editable=False, blank=True, null=False, verbose_name="Tarih")
    first_messsage = CharField(max_length=500, verbose_name="İlk Mesaj")

    class Meta:
        verbose_name = 'Sohbet'
        verbose_name_plural = 'Sohbetler'

    def __str__(self):
        return self.first_messsage



class Message(Model):
    chat = ForeignKey("FindBikeFriends_core.Chat",null=False, related_name='source_chat', on_delete=models.CASCADE, verbose_name="Sohbet")
    sent_user = ForeignKey("FindBikeFriends_core.User",null=False,related_name='source_user', on_delete=models.CASCADE, verbose_name="Gönderen Kişi")
    chat_message = CharField(max_length=500, verbose_name="Gönderilecek Mesajı")
    created_at = DateTimeField(auto_now_add=True, editable=False, blank=True, null=False, verbose_name="Tarih")

    class Meta:
        verbose_name = 'Sohbet Konuşması'
        verbose_name_plural = 'Sohbet Konuşmaları'

    def __str__(self):
        return "{}".format(self.pk)
