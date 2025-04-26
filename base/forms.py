from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'