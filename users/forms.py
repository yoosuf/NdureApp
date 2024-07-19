from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser, Invitation

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'timezone')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autofocus': True}))

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'timezone')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')
        
        
class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['email']

class InvitationAcceptanceForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'timezone', 'password1', 'password2')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2