from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, IntegerField, CharField, EmailField, DateField, ImageField
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer

from bitabak.utils import slugger, TZAwareModelSerializer
from bitabak_app.fields import LeximageField
from bitabak_app.models import User, Sofra, City, SofraImage, Meal, Order, \
    Address, MealType, CompanyFeature, Blog, BlogImage, BlogSofra, BlogComment
from bitabak_notification.models import Notification

from FindBikeFriends_core.models import User, Followers, EventTag, Event, City, CompanyAddress, CompanyFeature, Company, Advertisement, AdvertisementImage

class AddressSerializer(TZAwareModelSerializer):
    latlong = SerializerMethodField()

    def get_latlong(self, obj):
        return str(obj.lat) + "," + str(obj.long)

    class Meta:
        model = Address
        fields = ('name', 'open_address', 'postal_code', 'lat', 'long', 'latlong')


class RestaurantFeatureSerializer(TZAwareModelSerializer):
    icon = LeximageField()

    class Meta:
        model = CompanyFeature
        fields = '__all__'


class MealTypeSerializer(TZAwareModelSerializer):
    class Meta:
        model = MealType
        fields = ('name',)


class MealSerializer(TZAwareModelSerializer):
    type = MealTypeSerializer()

    class Meta:
        model = Meal
        fields = ('name', 'type')


class JoinSofraSerializer(Serializer):
    sofra = IntegerField()

    class Meta:
        fields = ('sofra',)


class SofraImageSerializer(TZAwareModelSerializer):
    class Meta:
        model = SofraImage
        fields = (
            'image',
            'sofra',
        )
        extra_kwargs = {
            'sofra': {'write_only': True},
        }


class UserSerializer(TZAwareModelSerializer):
    class PhoneSerializer(serializers.Field):
        def to_internal_value(self, data):
            return data

        def to_representation(self, value):
            if isinstance(self.parent.instance, list):
                if self.context['request'].user.pk in [x.pk for x in self.parent.instance]:
                    return value
            else:
                if hasattr(self.parent.instance, 'company') or self.context[
                    'request'].user.pk == self.parent.instance.pk:
                    return value
            return None

    sofras = SerializerMethodField(read_only=True)
    follow_count = SerializerMethodField(read_only=True)
    followers_count = SerializerMethodField(read_only=True)
    profile_photo = LeximageField()
    is_following = SerializerMethodField()
    features = SerializerMethodField(read_only=True)
    birthday = SerializerMethodField()
    phone = PhoneSerializer()
    address = SerializerMethodField()
    is_company = SerializerMethodField()

    def get_is_company(self, obj):
        return hasattr(obj, 'company')

    def get_is_following(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            if user in obj.followers.all():
                return True
        return False

    def get_sofras(self, obj):
        if hasattr(obj, 'company'):
            sofralar = Sofra.objects.filter(Q(owner__exact=obj) | Q(guests__in=[obj])).order_by(
                '-start_date').distinct()
        else:
            sofralar = Sofra.objects.filter(
                (Q(owner__exact=obj) | Q(guests__in=[obj])) & Q(end_date__lte=timezone.now())).order_by(
                '-start_date').distinct()
        return BasicSofraSerializer(sofralar, many=True, context={'request': self.context['request']}).data

    def get_email(self, obj):
        if hasattr(obj, 'company') or self.context['request'].user == obj:
            return obj.email

    def get_gender(self, obj):
        if hasattr(obj, 'company'):
            return obj.gender

    def get_address(self, obj):
        if hasattr(obj, 'company'):
            return AddressSerializer(obj.company.address).data

    def get_birthday(self, obj):
        if hasattr(obj, 'company') or self.context['request'].user == obj:
            return obj.birthday

    def get_features(self, obj):
        if hasattr(obj, 'company'):
            return RestaurantFeatureSerializer(obj.company.features, many=True).data

    def get_follow_count(self, obj):
        return User.objects.filter(followers__in=[obj]).count()

    def get_followers_count(self, obj):
        return obj.followers.count()

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'gender',
            'birthday',
            'phone',
            'email',
            'address',
            'profile_photo',
            'background_photo',
            'bio',
            'sofras',
            'follow_count',
            'followers_count',
            'is_following',
            'is_company',
            'features'
        )


class BasicUserSerializer(TZAwareModelSerializer):
    profile_photo = LeximageField()
    address = SerializerMethodField()
    is_company = SerializerMethodField()
    is_following = SerializerMethodField(read_only=True)

    def get_is_following(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            if user in obj.followers.all():
                return True
        return False

    def get_address(self, obj):
        if hasattr(obj, 'company'):
            return AddressSerializer(obj.company.address).data

    def get_is_company(self, obj):
        return hasattr(obj, 'company')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'profile_photo',
            'is_following',
            'is_company',
            'address'
        )


class BasicSofraSerializer(ModelSerializer):
    image = ImageField(source='get_first_image', read_only=True)
    owner = BasicUserSerializer()
    left_seat = SerializerMethodField()

    def get_left_seat(self, obj: Sofra):
        return obj.guest_limit - obj.guests.count()

    class Meta:
        model = Sofra
        fields = (
            'pk',
            'name',
            'image',
            'is_finished',
            'start_date',
            'left_seat',
            'owner'
        )


class SofraSerializer(TZAwareModelSerializer):
    owner = BasicUserSerializer()
    images = SofraImageSerializer(source='sofraimage_set', many=True)
    meals = MealSerializer(many=True)
    left_seat = SerializerMethodField()
    is_in_sofra = SerializerMethodField()

    def get_is_in_sofra(self, obj: Sofra):
        if self.context['request'].user in obj.guests.all():
            return True
        return False

    def get_left_seat(self, obj: Sofra):
        attendant_count = obj.guests.count()
        return obj.guest_limit - attendant_count

    class Meta:
        model = Sofra
        fields = (
            'pk',
            'name',
            'created',
            'last_updated',
            'description',
            'start_date',
            'end_date',
            'guest_limit',
            'price',
            'owner',
            'images',
            'left_seat',
            'meals',
            'is_finished',
            'is_expired',
            'is_in_sofra',
        )


class SendActivationSerializer(Serializer):
    email = CharField(max_length=100, label='Email')

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            return value
        except User.DoesNotExist:
            raise ValidationError('Bu emaile sahip bir kullanıcı bulunamadı.')


class RegistrationSerializer(Serializer):
    first_name = CharField(max_length=100, label='İsim')
    last_name = CharField(max_length=100, label='Soy İsim')
    email = EmailField(max_length=100, label='Email')
    bio = CharField(max_length=500, label='Biyografi', required=False)
    password1 = CharField(max_length=16, label='Şifre')
    password2 = CharField(max_length=16, label='Şifre Tekrar')
    gender = CharField(max_length=50, label='Cinsiyet', required=False)
    birthday = DateField(label='Doğum Tarihi')

    def validate(self, data):
        if data['password1'] == data['password2']:
            return data
        else:
            raise ValidationError('Girdiğiniz şifreler uyuşmamakta.')

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            raise ValidationError("Bu email kullanılmaktadır.")
        except User.DoesNotExist:
            return value

    def clear_name(self, name):
        return slugger(name).replace('-', '.')

    def create(self, validated_data):
        counter = 0
        first_name = self.clear_name(validated_data['first_name'])
        last_name = self.clear_name(validated_data['last_name'])

        while True:
            if counter == 0:
                username = '{}.{}'.format(first_name, last_name)
            else:
                username = '{}.{}{}'.format(first_name, last_name, counter)

            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                del validated_data['password2']
                validated_data['password'] = validated_data.pop('password1')

                return User.objects.create_user(username=username, is_verified=True, **validated_data)
            counter += 1

    def update(self, instance, validated_data):
        pass


class CitySerializer(TZAwareModelSerializer):
    class Meta:
        model = City
        fields = (
            'name',
            'number',
        )


class BlogImageSerializer(TZAwareModelSerializer):
    class Meta:
        model = BlogImage
        fields = ('image',)


class BlogSofraSerializer(TZAwareModelSerializer):
    sofra = SofraSerializer()

    class Meta:
        model = BlogSofra
        fields = ('sofra',)


class BlogCommentSerializer(TZAwareModelSerializer):
    class Meta:
        model = BlogComment
        fields = ('name_surname', 'photo', 'comment',)


class BlogSerializer(TZAwareModelSerializer):
    images = BlogImageSerializer(source='blogimage_set', many=True)
    sofras = BlogSofraSerializer(source='blogsofra_set', many=True)
    comments = BlogCommentSerializer(source='blogcomment_set', many=True)

    class Meta:
        model = Blog
        fields = (
            'title',
            'content',
            'read_count',
            'date',
            'images',
            'sofras',
            'comments',
        )


class BlogListSerializer(TZAwareModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'pk',
            'title',
            'thumbnail',
            'read_count',
            'date',
        )


class OrdersSerializer(TZAwareModelSerializer):
    sofra = SofraSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
            'sofra',
            'transaction_id',
            'transaction_total_amount',
            'transaction_time',
            'status',
            'coupon'
        )


class FollowSerializer(TZAwareModelSerializer):
    profile_photo = LeximageField(read_only=True)
    is_following = SerializerMethodField(read_only=True)

    def get_is_following(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            if user in obj.followers.all():
                return True
        return False

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'profile_photo',
            'is_following',
        )


class NotificationSerializer(ModelSerializer):
    actor = BasicUserSerializer()
    data_sofra = BasicSofraSerializer()

    class Meta:
        model = Notification
        fields = ('title', 'message', 'actor', 'data_sofra', 'created_at', 'read',)


class DeviceSerializer(Serializer):
    token = CharField(max_length=1000, label='Token', required=True)
    type = CharField(max_length=100, label='Type', required=True)
