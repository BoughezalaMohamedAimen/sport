from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from django.db.models import Q
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.core.paginator import Paginator



# Create your views here.
class HomeClient(TemplateView):
    def get(self,request):
        q = Q()
        if request.GET.get('nom'):
            for mot_cle in request.GET.get('nom').split(','):
                q |= Q(nom__contains=mot_cle)
                q |= Q(prenom__contains=mot_cle)
        if q:
            clients_list=Client.objects.filter(q).order_by('-id')
        else:
            clients_list=Client.objects.all().order_by('-id')

        paginator = Paginator(clients_list, 25) # Show 25 clients per page

        page = request.GET.get('page')
        clients = paginator.get_page(page)


        form_update=UpdateClientForm()
        return render(request,'clients/home.html',{'clients':clients,'form_update':form_update})

    def post(self,request):
        form=ClientForm(request.POST,request.FILES,prefix='add')
        form_update=UpdateClientForm()
        clients=Client.objects.all()
        if form.is_valid():
            form.save()
            form=ClientForm()
        return render(request,'clients/home.html',{'clients':clients,'form_update':form_update})


class UpdateClient(TemplateView):
    def get(self,request,id):
        client=Client.objects.get(id=id)
        form_update=UpdateClientForm(instance=client)
        last_seance=SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[0]
        context={'form_update':form_update,'client':client,'last_seance':last_seance}
        return render(request,'clients/update_client.html',context)

    def post(self,request,id):
        form_update=UpdateClientForm(request.POST,request.FILES,prefix='update',instance=Client.objects.get(id=id))
        if form_update.is_valid():
            form_update.save()
        return redirect('home_clients')


class GetClient(TemplateView):
    def post(self,request):
        try:
            client=Client.objects.get(rfid=request.POST.get('rfid'));
        except:
            client=Client.objects.get(id=request.POST.get('rfid'));

        form_update=UpdateClientForm(instance=client)
        last_seance=SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[0]
        context={'form_update':form_update,'client':client,'last_seance':last_seance}
        return render(request,'clients/update_client.html',context)

def MarquerSeance(request,id):
    client=Client.objects.get(id=id)
    client.consome()
    return HttpResponse(status=200)


def GetHistorique(request,id):
    client=Client.objects.get(id=id)
    historique_list=SeanceHistorique.objects.filter(client=client).order_by('-date_heure')
    paginator = Paginator(historique_list, 10) # Show 25 clients per page
    page = request.GET.get('page')
    historiques = paginator.get_page(page)
    return render(request,'clients/historique_client.html',{'historiques':historiques})
