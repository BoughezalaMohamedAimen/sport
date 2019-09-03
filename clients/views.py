from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import *
from django.db.models import Q
from datetime import datetime
# Create your views here.
class HomeClient(TemplateView):
    def get(self,request):
        form_update=UpdateClientForm()

        clients=Client.objects.all()
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
        form_update=UpdateClientForm(instance=Client.objects.get(id=id))
        return render(request,'clients/update_client.html',{'form_update':form_update})

    def post(self,request,id):
        form_update=UpdateClientForm(request.POST,request.FILES,prefix='update',instance=Client.objects.get(id=id))
        if form_update.is_valid():
            form_update.save()
        return redirect('home_clients')
