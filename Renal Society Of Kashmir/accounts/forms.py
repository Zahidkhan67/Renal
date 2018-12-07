from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User         

class SignUpForm(UserCreationForm):
            username = forms.CharField(max_length=30, required=False, help_text='Enter Your Name.')
            fullname = forms.CharField(max_length=30, required=False, help_text='Enter Your Name.')
            address = forms.CharField(max_length=30, required=False, help_text='Enter Your Name.')
            phone = forms.DecimalField(decimal_places=13, required=True, help_text='Required.')
            email = forms.EmailField(max_length=40, help_text='Required. Inform a valid email address.')

            class Meta:
                        model = User
                        fields = ( 'username','fullname','address','phone','email','username', 'password1', 'password2',   )