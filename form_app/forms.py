from django import forms
from django.forms.formsets import formset_factory

class NameForm(forms.Form):
	name = forms.CharField(label='Name', required=True)

NameFormSet = formset_factory(NameForm)