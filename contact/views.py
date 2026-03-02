from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Contact, ContactMessage


def contact_page(request):
    contact_info = Contact.objects.first()

    if request.method == 'POST':
        ContactMessage.objects.create(
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
        )
        messages.success(request, "Xabaringiz yuborildi. Tez orada javob beramiz.")
        return redirect('contact:contact')

    return render(request, 'contact/contact.html', {'contact_info': contact_info})