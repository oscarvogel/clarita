from django import forms
from django.contrib.auth.models import User

from apps.account.models import Profile


class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Usuario'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Contraseña'
    }))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': u'Contraseña'
    }))
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': u'Repetir Contraseña'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(u'Contraseñas no coinciden.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nacimiento', 'foto')