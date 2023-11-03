from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={# "placeholder": "Username",
                                                             # "style": "width: 200px;",
                                                             "class": "form-control input-widget"}),
                               label="Username",
                               max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={# "placeholder": "Password",
                                                                 # "style": "width: 200px;",
                                                                 "class": "form-control input-widget"}),
                              label="Password",
                               max_length=100)

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control input-widget"}),
        label="First Name",
        max_length=30
)

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control input-widget"}),
        label = "Last Name",
        max_length=30
)

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control input-widget"}),
        label="Username",
        max_length=30
)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control input-widget"}),
        label="Password",
        max_length=100
)