from django  import forms
from .models import Neighborhood,Business,MyUser,Post

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        exclude = ['user']