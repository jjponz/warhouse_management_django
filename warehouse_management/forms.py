from django import forms
from .models import ItemMapper

class ItemForm(forms.ModelForm):
    name = forms.CharField(required=False)
    notes = forms.CharField(required=False)

    class Meta:
        model = ItemMapper
        fields = ('name', 'notes')



