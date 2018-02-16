from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm, DatasetSubmitForm

def contactView(request):
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            cd = contactForm.cleaned_data
            subject = cd['subject']
            message = cd['message']
            from_email = cd['from_email']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('sendemail:success')
    else:
        contactForm = ContactForm()
    return render(request, 'sendemail/email.html', {'contactForm': contactForm})


def submitDatasetView(request):
    if request.method == 'POST':
        datasetSubmitForm = DatasetSubmitForm(request.POST)
        if datasetSubmitForm.is_valid():
            cd = datasetSubmitForm.cleaned_data
            title = cd['title']
            description = cd['description']
            context = cd['context']
            contact_details = cd['contact_details']
            try:
                send_mail(title, description, contact_details, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('sendemail:success')
    else:
        datasetSubmitForm = DatasetSubmitForm()
    return render(request, 'sendemail/datasetSubmit.html', {'datasetSubmitForm': datasetSubmitForm})


def successView(request):
    return render(request, 'sendemail/success.html')

