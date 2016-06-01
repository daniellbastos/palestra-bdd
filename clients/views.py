from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views import generic

from clients.forms import ClientForm
from clients.models import Client


class ClientCreateView(generic.CreateView):
    template_name = 'clients/client_form.html'
    form_class = ClientForm
    model = Client

    def get_success_url(self):
        messages.success(self.request, 'Cliente cadastrado com sucesso.')
        return reverse('clients:client-list')


class ClientListView(generic.ListView):
    template_name = 'clients/client_list.html'
    queryset = Client.objects.actives()


class InactiveClientListView(generic.ListView):
    template_name = 'clients/inactive_client_list.html'
    queryset = Client.objects.filter(is_active=False)
