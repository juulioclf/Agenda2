from django.shortcuts import render
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contatos/index.html', {
        'contacts': contacts
    })


def search_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contatos/search_contact.html', {
        'contact': contact
    })