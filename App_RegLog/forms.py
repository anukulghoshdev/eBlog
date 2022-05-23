from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from App_RegLog.models import UserInfo
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class profile_pic(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['profile_pic']
