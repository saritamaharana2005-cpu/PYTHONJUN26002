from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]       
        
        extra_kward = {
            'password' : {'write_only':True}
        }
        
    def  create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password']
        )
        
        return user