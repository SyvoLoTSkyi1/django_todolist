from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# todo remove
class LoginModelForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        required=True
    )
    error_massages = {'error': 'Wrong username or password'}

    class Meta:
        model = User
        fields = ('username', 'password')

    def is_valid(self):
        if not self.errors:
            self.user = authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password']
            )
            if not self.user:
                self.errors.update(self.error_massages)

        return super().is_valid()


class SignUpModelForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(),
        required=True
    )
    username = forms.CharField(
        label='Username',
        required=True,
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        required=True
    )
    password2 = forms.CharField(
        label='Password Again',
        widget=forms.PasswordInput(),
        required=True
    )
    error_massages = {'password_error': 'Passwords don\'t match'}

    class Meta:
        model = User
        fields = ('email', 'username',  'password1', 'password2')

    def is_valid(self):
        if not self.errors:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 != password2:
                self.errors.update(self.error_massages)

        return super().is_valid()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
