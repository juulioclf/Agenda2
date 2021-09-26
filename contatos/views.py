from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contacts': contacts
    })


def search_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contatos/search_contact.html', {
        'contact': contact
    })




