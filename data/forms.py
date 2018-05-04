from django import forms
from .models import DataSet, Type, Scale, Parameter, Outcome, Time, FuturesModeling


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=50, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Search for datasets and models'}))


class QueryForm(forms.ModelForm):
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.RadioSelect,
        required=False,
    )
    spatial_scales = forms.ModelMultipleChoiceField(
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
    time = forms.ModelMultipleChoiceField(
        queryset=Time.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    futures_modeling = forms.ModelMultipleChoiceField(
        queryset=FuturesModeling.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = DataSet
        fields = ['type', 'scales', 'parameters', 'outcomes']


class DatasetSubmitForm(forms.ModelForm):
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )
    title = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Dataset Title'}))
    description = forms.CharField(required=True, max_length=200, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                              'placeholder': 'Description'}))
    context = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Context'}))
    key_takeaways = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                'placeholder': 'Key Takeaways'}))
    sample_uses_and_visualization = forms.CharField(required=True, max_length=50,
                                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Sample Uses and Visualization'}))
    technical_details = forms.CharField(required=True, max_length=50,
                                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Technical Details'}))
    applicable_models_or_datasets = forms.CharField(required=True, max_length=50,
                                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Applicable Models or Datasets'}))
    relevant_publications = forms.CharField(required=True, max_length=50,
                                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Relevant Publications'}))
    owner = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Your Name'}))
    contact_details = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'your@email.com'}))
    scales = forms.ModelMultipleChoiceField(
        queryset=Scale.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    parameters = forms.ModelMultipleChoiceField(
        queryset=Parameter.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    outcomes = forms.ModelMultipleChoiceField(
        queryset=Outcome.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    time = forms.ModelMultipleChoiceField(
        queryset=Time.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    futures_modeling = forms.ModelMultipleChoiceField(
        queryset=FuturesModeling.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = DataSet
        fields = ['title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                  'technical_details', 'applicable_models_or_datasets', 'relevant_publications', 'owner',
                  'contact_details', 'scales', 'parameters', 'outcomes', 'type']
