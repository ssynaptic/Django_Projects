from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={# "placeholder": "Username",
                                                             "style": "width: 200px;",
                                                             "class": "form-control input-widget"}),
                               label="Username",
                               max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={# "placeholder": "Password",
                                                                 "style": "width: 200px;",
                                                                 "class": "form-control input-widget"}),
                              label="Password",
                               max_length=100)