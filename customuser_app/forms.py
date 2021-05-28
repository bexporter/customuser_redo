from django import forms
from customuser_app.models import MyUser


class SignUp(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'password',
            'homepage',
            'email',
            'age',
            'displayname',]

class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser 
        fields = [
            'username',
            'password',]