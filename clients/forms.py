from django import forms
from .models import *
import datetime
class ClientForm(forms.ModelForm):
    prefix = 'add'
    date_naissance = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )
    class Meta:
            model=Client
            fields='__all__'

class UpdateClientForm(forms.ModelForm):
    prefix = 'update'
    date_naissance = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y', ))
    date_debut = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y', ))
    date_fin = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y', ))
    class Meta:
            model=Client
            fields='__all__'

class AbonnementForm(forms.ModelForm):
    prefix='abonnement'
    date_debut = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y', ),initial=datetime.date.today())
    class Meta:
        model=Abonnement
        fields='__all__'
