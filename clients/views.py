from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from django.db.models import Q
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.contrib.humanize.templatetags.humanize import naturaltime,naturalday
import os
import _thread
from .speech import *

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
            _thread.start_new_thread( TextSpeak, ("Nouveau  client ajouté.",) )
            form=ClientForm()
        return render(request,'clients/home.html',{'clients':clients,'form_update':form_update})


class UpdateClient(TemplateView):
    def get(self,request,id):
        client=Client.objects.get(id=id)
        try:
            last_seance=SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[0]
        except:
            last_seance=''
        context={
        'form_update':UpdateClientForm(instance=client),
        'client':client,
        'last_seance':last_seance,
        'abonnement_form':AbonnementForm(),
        'caisseday':Caisse.objects.get(date=datetime.date.today())
        }
        return render(request,'clients/update_client.html',context)

    def post(self,request,id):
        form_update=UpdateClientForm(request.POST,request.FILES,prefix='update',instance=Client.objects.get(id=id))
        if form_update.is_valid():
            form_update.save()
            _thread.start_new_thread( TextSpeak, ('Les informations du client ont bien été sauvegardé',) )
        return redirect('home_clients')


class GetClient(TemplateView):
    def post(self,request):

        try:
            client=Client.objects.get(rfid=request.POST.get('rfid'));
            _thread.start_new_thread( speak, (client,) )
            return redirect ('update_clients',client.id)
        except Exception as e:
            print(e)
            try:
                client=Client.objects.get(id=request.POST.get('rfid'));
                _thread.start_new_thread( speak, (client,) )
                return redirect ('update_clients',client.id)
            except:
                pass
        return HttpResponseNotFound('Client Inexistant')



def MarquerSeance(request,id):
    try:
        client=Client.objects.get(id=id)
        client.consome()
        _thread.start_new_thread( TextSpeak, ('La Séance a bien été Marqué',) )
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        SeanceHistorique(versement=request.GET.get('versement'),nom=request.GET.get('nom')).save()
        caisse=Caisse.objects.get(date=datetime.date.today())
        caisse.fermeture_prevu+=int(request.GET.get('versement'))
        caisse.save()
        _thread.start_new_thread( TextSpeak, ('Nouvelle séance Libre sauvegardé',) )
        return redirect ('home_clients')



def AnullerSeance(request,id):
    seance=SeanceHistorique.objects.get(id=id)
    if seance.client:
        seance.client.seance+=1
        seance.client.save()
        seance.delete()
        _thread.start_new_thread( TextSpeak, ('La séance a bien été, anullé.',) )
        return redirect('historique_page_num',seance.client.id )
    else:
        seance.delete()
        caisse=Caisse.objects.get(date=seance.date_heure)
        caisse.fermeture_prevu-=seance.versement
        caisse.save()
        _thread.start_new_thread( TextSpeak, ('La séance a bien été, anullé.',) )
        return redirect('historique_seance_libre_page_num',caisse.id )





def GetHistorique(request,id=0):
    try:
        client=Client.objects.get(id=id)
        historique_list=SeanceHistorique.objects.filter(client=client).order_by('-date_heure')
    except ObjectDoesNotExist:
        historique_list=SeanceHistorique.objects.filter(client=None).order_by('-date_heure')
    paginator = Paginator(historique_list, 10) # Show 25 clients per page
    page = request.GET.get('page')
    historiques = paginator.get_page(page)
    return render(request,'clients/historique_client.html',{'historiques':historiques})




def GetHistoriquePayement(request,id=0):
    try:
        client=Client.objects.get(id=id)
        historique_list=Abonnement.objects.filter(client=client).order_by('-date_heure')
    except:
        historique_list=Abonnement.objects.filter(client=None).order_by('-date_heure')
    paginator = Paginator(historique_list, 10) # Show 25 clients per page
    page = request.GET.get('page')
    historiques_payements = paginator.get_page(page)
    return render(request,'clients/historique_payement.html',{'historiques_payements':historiques_payements})


class UpdateClientAbonement(TemplateView):
    def post(self,request,id):
        client=Client.objects.get(id=id)
        abonnement_form=AbonnementForm(request.POST,prefix='abonnement')
        if abonnement_form.is_valid():
            client.renouvler(abonnement_form.cleaned_data['date_debut'],abonnement_form.cleaned_data['forfait'],abonnement_form.cleaned_data['nbr_mois'])
            abonnement_form.save()
            _thread.start_new_thread( TextSpeak, ('Nouveau Forfait  '+str(abonnement_form.cleaned_data['forfait'])+'Activé',) )
        return redirect('home_clients')


class DeleteClientAbonement(TemplateView):
    def get(self,request,id):
        abonement=Abonnement.objects.get(id=id)
        abonement.delete()
        _thread.start_new_thread( TextSpeak, ("L'abonnement a bien été anullé, anullé.",) )
        return redirect('historique_payment_page_num',abonement.client.id)
