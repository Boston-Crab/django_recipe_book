from django import forms 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove labels
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
        
        self.fields['username'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Your Password'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Confirm Password'
        })

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter New Email'
        }),
        label = ''
    )

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2',]

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Username'
        }),
        label = ''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Password'
        }),
        label = ''
    )

class EmailChangeForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter New Email'
        }),
        label = ''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter Your Password'
        }),
        label = ''
    )

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError('Password is incorrect.')
        return password

    def save(self, commit=True):
        self.user.email = self.cleaned_data['email']
        if commit:
            self.user.save()
        return self.user
    
class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove labels
        self.fields['old_password'].label = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password2'].label = ''
        
        self.fields['old_password'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Your Password'
        })

        self.fields['new_password1'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'New Password'
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Confirm New Password'
        })