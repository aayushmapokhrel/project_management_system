from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import ValidationError

from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=True)
    class Meta:
        model = User
        fields = ['username','password','email']

    def validate(self,validated_data):
        user = validated_data['username']
        if len(user)<8:
            raise ValidationError({
                "username":"Username should be more 8 cha"
            })
        return validated_data
    
    def validate_password(self, password):
        if len(password)<5:
             raise ValidationError({
                "password":"password should be more 8 cha"
            })
        return password



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

    def to_representation(self, instance):
        token = RefreshToken.for_user(instance)
        data = super().to_representation(instance)
        data['access_token']=str(token.access_token)
        data['refresh_token']=str(token)
        return data
    

class ChangePassword(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


    # def validate(self, validated_data):
    #     if validated_data['new_password']!=validated_data['confirm_password']:
    #         raise ValidationError("new password and confirm password mush be same ")
        
    #     if old_password == new_password:
    #         new password should not be same 

    #     check_password(passwrd ) not = old_password 


    # user.set_password(data[''])



