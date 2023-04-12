from rest_framework import fields, serializers
from .models import User, Category, OrderStatus, Order, Media, OrderPhoto, OrderVideo, UserReview, UserReviewPhoto, UserReviewVideo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("name", "surname", "patronimic", "phone_number", "email", "about", "city", "avatar", "role")


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

