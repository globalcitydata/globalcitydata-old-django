from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'your@email.com'}))
    subject = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Subject'}))
    message = forms.CharField(required=True, max_length=200, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Message'}))

class DatasetSubmitForm(forms.Form):
    title = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Dataset Title'}))
    description = forms.CharField(required=True, max_length=200, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Description'}))
    context = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Context'}))
    key_takeaways = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Key Takeaways'}))
    sample_uses_and_visualization = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Sample Uses and Visualization'}))
    technical_details = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Technical Details'}))
    applicable_models = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Applicable Models'}))
    relevant_publications = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Relevant Publications'}))
    owner = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Your Name'}))
    contact_details = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'your@email.com'}))
