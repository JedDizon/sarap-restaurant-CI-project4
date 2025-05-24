from django.shortcuts import render
from .models import Contact
# from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect


def contact_page(request):
    contact = Contact.objects.all().order_by('-updated_on').first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"Received message from {name} ({email} - {phone}): {subject} - {message}")
        messages.success(request, "Thanks! Your message has been received.", extra_tags="contact")
        return redirect('contact')

    return render(request, "contact/contact.html", {"contact": contact})