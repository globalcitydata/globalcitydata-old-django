from django import forms
from .models import DataSet, Scale, Parameter, Outcome


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=50, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Search for datasets'}))


class QueryForm(forms.ModelForm):
    scales = forms.ModelMultipleChoiceField(
        queryset=Scale.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    parameters = forms.ModelMultipleChoiceField(
        queryset=Parameter.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    outcomes = forms.ModelMultipleChoiceField(
        queryset=Outcome.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = DataSet
        fields = ['scales', 'parameters', 'outcomes']
