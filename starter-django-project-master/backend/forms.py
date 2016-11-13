from django import forms

class SolutionForm(forms.Form):
    solution = forms.CharField(initial="#########################", max_length=100)
