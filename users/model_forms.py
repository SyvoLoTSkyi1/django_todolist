from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email", "username"
        )
        field_classes = {
            'email': forms.EmailField,
            'username': UsernameField,
        }

        def clean(self):
            self.instance.is_active = False
            return self.cleaned_data
