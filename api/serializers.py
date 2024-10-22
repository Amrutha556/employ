from rest_framework import serializers
from api.models import User,empoly


class employModelSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=empoly
        fields="__all__"




class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    # this is used to hide the create.
    
    