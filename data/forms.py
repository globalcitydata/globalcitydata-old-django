from django import forms
from .models import DataSet, Type, Scale, Parameter, Outcome


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
        fields = ['type', 'scales', 'parameters', 'outcomes']


class DatasetSubmitForm(forms.ModelForm):
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
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = DataSet
        fields = ['title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                  'technical_details', 'applicable_models_or_datasets', 'relevant_publications', 'owner',
                  'scales', 'parameters', 'outcomes', 'type']
