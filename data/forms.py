from django.forms import ModelForm, CheckboxSelectMultiple, ModelMultipleChoiceField
from .models import DataSet, Scale, Parameter, Outcome


# class SearchForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SearchForm, self).__init__(*args, **kwargs)
#         for key, field in self.fields.iteritems():
#             self.fields[key].required = False

class DataSetForm(ModelForm):
    scales = ModelMultipleChoiceField(
        queryset=Scale.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )
    parameters = ModelMultipleChoiceField(
        queryset=Parameter.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )
    outcomes = ModelMultipleChoiceField(
        queryset=Outcome.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = DataSet
        fields = ['scales', 'parameters', 'outcomes']
