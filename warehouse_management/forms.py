from django import forms
from .models import ItemMapper

class ItemForm(forms.ModelForm):
    name = forms.CharField(required=False)
    notes = forms.CharField(required=False)

    class Meta:
        model = ItemMapper
        fields = ('name', 'notes')

class ItemFinderForm(forms.Form):
    property = forms.CharField(required=False)
    value = forms.CharField(required=False)

