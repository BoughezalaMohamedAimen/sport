from .forms import ClientForm
def add_client_form_to_context(request):
    cart=ClientForm()
    return {
        'AddClientForm': ClientForm
    }
