from django import forms
from .models import DataSet, Type, Scale, Parameter, Outcome, Time, WorldRegions


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=50, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Search for datasets and models'}))


class QueryForm(forms.ModelForm):
    content_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.RadioSelect,
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
    spatial_scales = forms.ModelMultipleChoiceField(
        queryset=Scale.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    temporal_scales = forms.ModelMultipleChoiceField(
        queryset=Time.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    world_regions = forms.ModelMultipleChoiceField(
        queryset=WorldRegions.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = DataSet
        fields = ['content_type', 'parameters', 'outcomes', "spatial_scales", 'temporal_scales', 'world_regions']


class DatasetSubmitForm(forms.ModelForm):
    content_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )
    title = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Dataset Title'}))
    description = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                              'placeholder': 'Description'}))
    context = forms.CharField(required=True, max_length=750, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Context'}))
    key_takeaways = forms.CharField(required=True, max_length=750, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                'placeholder': 'Key Takeaways'}))
    sample_uses_and_visualization = forms.CharField(required=True, max_length=100,
                                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Sample Uses and Visualization'}))
    technical_details = forms.CharField(required=True, max_length=750,
                                        widget=forms.Textarea(attrs={'class': 'form-control',
                                                                      'placeholder': 'Technical Details'}))
    applicable_models_or_datasets = forms.CharField(required=True, max_length=750,
                                        widget=forms.Textarea(attrs={'class': 'form-control',
                                                                      'placeholder': 'Applicable Models or Datasets'}))
    relevant_publications = forms.CharField(required=True, max_length=750,
                                            widget=forms.Textarea(attrs={'class': 'form-control',
                                                                          'placeholder': 'Relevant Publications'}))
    owner = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Your Name'}))
    contact_details = forms.EmailField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'your@email.com'}))
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
    spatial_scales = forms.ModelMultipleChoiceField(
        queryset=Scale.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    temporal_scales = forms.ModelMultipleChoiceField(
        queryset=Time.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    world_regions = forms.ModelMultipleChoiceField(
        queryset=WorldRegions.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = DataSet
        fields = ['content_type', 'title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                  'technical_details', 'applicable_models_or_datasets', 'relevant_publications', 'owner',
                  'contact_details', 'parameters', 'outcomes', "spatial_scales", 'temporal_scales', 'world_regions']
