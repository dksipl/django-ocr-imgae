from django import forms
from django.forms import ClearableFileInput
from app1.models import UserUploadModel

class UserUploadForm(forms.ModelForm):
    

    class Meta:

        model = UserUploadModel
        fields = ['file']
        widgets = {
            'file' : ClearableFileInput(attrs = {'multiple': True}),
        }