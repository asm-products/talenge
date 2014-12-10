__author__ = 'ranveer'

from django import forms
from django.contrib.auth.models import User
from authentication.models import UserProfile

class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': 'Username'
            }
        ),
        required=True,
        error_messages={
            'required': 'A username is required'
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password',
                'placeholder': 'Password'
            }
        ),
        required=True,
        error_messages={
            'required': 'A password is required'
        }
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'E-Mail ID'
            }
        ),
        required=True,
        error_messages={
            'required': 'An E-mail ID is required'
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    USER_TYPE_CHOICES = (
        ('s', 'Student'),
        ('c', 'Company' ),
    )

    website = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'website',
                'placeholder': 'Web URL'
            }
        ),
        required=False,
    )

    picture = forms.ImageField(
        required=False,
        widget = forms.FileInput(
            attrs={
                'class': 'btn btn-primary',
                'id': 'image'
            }
        ),
    )

    type_user = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class':'form-control',
                'id': 'usertype',
            }
        ),
        required=True,
    )

    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'type_user')