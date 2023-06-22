from django import forms

class LaptopModelFilterForm(forms.Form):
    model = forms.CharField()