from django import forms
from users.models import UserAccount

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={

    }),
    label="First Name",
    max_length=255)

    last_name = forms.CharField(widget=forms.TextInput(attrs={

    }),
    label="Last Name",
    max_length=255)

    username = forms.CharField(widget=forms.TextInput(attrs={

    }),
    label="Username",
    max_length=255)

    password = forms.CharField(widget=forms.PasswordInput(attrs={

    }),
    label="Password",
    max_length=255)

    class Meta:
        model = UserAccount
        fields = ["first_name", "last_name", "username", "password"]

class LogInForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-input",
        "aria-describedby": "Username of the account"
    }),
    label="Username",
    max_length=255)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-lg form-input",
        "aria-describedby": "Password of the account"
    }),
    label="Password",
    max_length=255)

    class Meta:
        model = UserAccount
        fields = ["username", "password"]

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()