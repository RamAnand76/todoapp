from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



"""class TodoItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']"""


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = 'Username'  # Update the label text and style
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].label = 'Email'
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['passwoed1'].label = 'Password'
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].label = 'Re Enter Password'  # Update the label text and style
        # Similarly, update label and style for other fields


    """def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data"""