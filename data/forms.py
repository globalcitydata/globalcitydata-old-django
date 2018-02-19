from django import forms
from .models import DataSet, DataSetModel, Scale, Parameter, Outcome


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=50, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Search for datasets'}))


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


class DatasetModelForm(forms.ModelForm):
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
        model = DataSetModel
        fields = ['scales', 'parameters', 'outcomes']


class DatasetSubmitForm(forms.ModelForm):
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
        fields = ['title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                  'technical_details', 'applicable_models', 'relevant_publications', 'owner',
                  'scales', 'parameters', 'outcomes']


class DatasetModelSubmitForm(forms.ModelForm):
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
        model = DataSetModel
        fields = ['title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                  'technical_details', 'applicable_models', 'relevant_publications', 'owner',
                  'scales', 'parameters', 'outcomes']