from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=100, widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm password", max_length=100, widget = forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
              raise ValidationError('Email already exist')
        return(email)

    def clean_username(self):
        username = self.cleaned_data['username']
        q = User.objects.filter(username=username)
        if q.exists():
              raise ValidationError('Username already exist')
        return(username)

    #it is used to show field error i.e. error will show above the field
    #def cleane_password2(self):
        #p1 = self.cleaned_data['password1']
        #p2 = self.cleaned_data['password2']
        #if p1 != p2:
            #raise ValidationError("password don't match")
        #return(p2)

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('password Do Not Match')
        