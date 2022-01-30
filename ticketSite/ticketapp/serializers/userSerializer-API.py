from django.contrib.admin.models import User
from tickets.serializers import UserSerializer

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100, style={"input_type":"password"})
    is_staff = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """The function called when you create a new User object/instance"""

# validated the objects instance        
        return User.objects.create(**validated_data)

# updating & creating our User Instance     
    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.

        """
        
# Update & Returning an existing user instance given Validated_data method().
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance

