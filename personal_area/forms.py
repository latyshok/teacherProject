from django import forms


class AuthForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput({
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'form-control'
    }))
