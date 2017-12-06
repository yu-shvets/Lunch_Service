from registration.forms import RegistrationFormUniqueEmail
from django import forms


class ProfileForm(RegistrationFormUniqueEmail):

    phone = forms.CharField(max_length=256)
    email = forms.EmailField()
