from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone',]

    def save(self, **kwargs):
        self.is_valid()
        email = self.validated_data.get('email')
        user, created = User.objects.get_or_create(email=email, defaults=self.validated_data)
        if not created:
            user.fam = self.validated_data.get('fam')
            user.name = self.validated_data.get('name')
            user.otc = self.validated_data.get('otc')
            user.phone = self.validated_data.get('phone')
            user.save()
        return user


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title')


class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        depth = 1
        fields = ['pk', 'status', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'user', 'coords', 'level', 'images']
        read_only_fields = ['pk', 'status', 'add_time']


    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        pass_user = User.objects.filter(email=user['email'])
        if pass_user.exists():
            user_serializer = UserSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
        else:
            user = User.objects.create(**user)

        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level, status='new')

        for image in images:
            data = image.pop('data')
            title = image.pop('title')
            Images.objects.create(data=data, pereval=pereval, title=title)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
            ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
        return data
