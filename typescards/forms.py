from django import forms

from .models import Types

class TypesForm(forms.ModelForm):

    class Meta:
        model = Types
        fields = ('name', 'description', 'year', 'category')