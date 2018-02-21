from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'your@email.com'}))
    subject = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Subject'}))
    message = forms.CharField(required=True, max_length=200, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Message'}))

