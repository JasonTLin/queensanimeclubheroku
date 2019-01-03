from django.shortcuts import render, redirect
from .forms import ContactForm, LoggedinForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message'] + " sent by " + sender_email
            send_mail(subject, message, ['queens.anime@gmail.com'], ['queens.anime@gmail.com'])
            messages.success(request, "Message successfully sent")
        return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
