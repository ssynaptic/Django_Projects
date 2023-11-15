from django import forms

class AccountCreationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
          "class": "creation-form-field"
        }),
        label="First Name",
        max_length=30
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
          "class": "creation-forms-field"
        }),
        label="Last Name",
        max_length=30
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
          "class": "creation-form-field"
        }),
        label="Username",
        max_length=50
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
          "class": "creation-form-field"
        }),
        label="Password",
        max_length=256
    )