from rest_framework import fields, serializers
from .models import Category, OrderStatus, Order, Media, OrderPhoto, OrderVideo, UserReview, UserReviewPhoto, UserReviewVideo, User, Contractor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "surname", "patronimic", "phone_number", "email", "about", "city", "avatar")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "photo")


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ("status")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("title", "detail", "author", "status")


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("file", "source")


class OrderPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPhoto
        fields = ("file", "source")


class OrderVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderVideo
        fields = ("file", "source")


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ("title", "detail", "rate", "user")


class UserReviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewPhoto
        fields = ("file", "source")


class UserReviewVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewVideo
        fields = ("file", "source")


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ("name", "surname", "patronimic", "phone_number", "email", "about", "city", "avatar")


class RegistrationUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['name', 'surname', 'patronimic', 'email', 'phone_number', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            patronimic=self.validated_data['patronimic'],
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.password = password
        user.save()
        return user


class RegistrationContractorSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = Contractor
        fields = ['name', 'surname', 'patronimic', 'email', 'phone_number', 'password', 'password2']

    def save(self, *args, **kwargs):
        contractor = Contractor(
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            patronimic=self.validated_data['patronimic'],
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        contractor.password = password
        contractor.save()
        return contractor


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email', 'password'],
        )
        email = self.validated_data['email'],
        password = self.validated_data['password']
        if User.objects.get(email=email) != email:
            raise serializers.ValidationError({password: "Логин не совпадает"})
        if User.objects.get(password=password) != password:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.password = password
        user.save()
        return User


class LoginContractorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contractor
        fields = ['email', 'password']

    def save(self, *args, **kwargs):
        contractor = Contractor(
            email=self.validated_data['email', 'password'],
        )
        email = self.validated_data['email'],
        password = self.validated_data['password']
        if Contractor.objects.get(email=email) != email:
            raise serializers.ValidationError({password: "Логин не совпадает"})
        if Contractor.objects.get(password=password) != password:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        contractor.password = password
        contractor.save()
        return contractor
