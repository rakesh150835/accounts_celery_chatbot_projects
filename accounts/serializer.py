from rest_framework import serializers

from .models import User


class RegisterSerailizer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']
        

    def validate(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords do not match!')
        
        return validated_data
    
    
    


class LoginSerailizer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
        

    