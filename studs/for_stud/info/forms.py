from django import forms
from .models import Info
from django.forms import ModelForm


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    user_data = Info.objects.filter(username="username").all()
    if user_data:
        return user_data.username
    else:
        raise forms.ValidationError("Error found")
