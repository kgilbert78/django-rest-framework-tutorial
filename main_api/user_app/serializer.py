from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from main_api import settings
from .models import User

# used when registering a new user only
class RegisterSerializer(serializers.Serializer):
    # email requirement coded this way needs to be specified at bottom of settings.py w/this variable name
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)

    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    
    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(("The passwords you entered don't match."))
        return data
    
    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'user_type': self.validated_data.get('user_type', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

# serialize the data from users' posts and gets to api
class UserDetailsSerializer(serializers.ModelSerializer):
    # user model without password
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'about_me') # temporarily removed 'profile_img'
        read_only_fields = ('email', )