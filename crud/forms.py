from django import forms
from .models import crud2

class crud2Form(forms.ModelForm):
    class Meta:
        model = crud2
        fields = '__all__'