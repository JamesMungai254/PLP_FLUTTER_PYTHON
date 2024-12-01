from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Parent, Facilitator
from vaccination.models import Child 

class ParentSignUpForm(UserCreationForm):
    parent_id = forms.CharField(
        max_length=100,
        label="Parent ID",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Parent ID'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'parent_id']
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_parent = True
        if commit:
            user.save()
            Parent.objects.create(user=user, parent_id=self.cleaned_data['parent_id'])
        return user

class FacilitatorSignUpForm(UserCreationForm):
    secret_key = forms.CharField(
        max_length=50,
        label="Secret Key",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Secret Key'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'secret_key']
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_facilitator = True
        if commit:
            user.save()
            Facilitator.objects.create(user=user, secret_key=self.cleaned_data['secret_key'])
        return user
# accounts/forms.py

class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['full_name']  # Add other fields if necessary



