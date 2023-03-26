from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        is_vendor = self.context['request'].data.get('is_vendor', None)
        if not is_vendor:
            # If user is not a vendor, or it's a new user, only require these fields
            self.fields['username'].required = True
            self.fields['email'].required = True
            self.fields['password'].required = True
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            # Set other fields to not required
            self.fields['shop_name'].required = False
            self.fields['shop_url'].required = False
            self.fields['company_name'].required = False
            self.fields['company_url'].required = False
            self.fields['company_id'].required = False
            self.fields['tax_number'].required = False
            self.fields['bank_number'].required = False
            self.fields['bank_iban'].required = False
            self.fields['phone_number'].required = False

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ('password',)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=64)
    password = serializers.CharField(required=True, max_length=64)

    default_error_messages = {
        'invalid_old_password': 'Old password is invalid'
    }

    def validate_old_password(self, password):
        if not check_password(password, self.instance.password):
            raise serializers.ValidationError(self.error_messages['invalid_old_password'])

        return password

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
