from django import forms

from WebBasicsExam.user_profile.models import Profile


class ProfileBaseFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs = {'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs ={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs = {'placeholder': 'Email'}),
            'password': forms.TextInput(attrs = {'placeholder': 'Password'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = False

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')

