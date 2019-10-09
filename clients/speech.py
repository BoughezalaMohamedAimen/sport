import pyttsx3
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import SeanceHistorique
def speak(client):
    try:
        last_seance=", dernière présence : "+str(naturaltime(SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[0].date_heure))
    except Exception as e:
        print(e)
        last_seance=''
    Text ="Bienvenue! "+client.nom+" "+client.prenom+". \n "+last_seance+". \n Abonnement  "+client.actif_abonement().forfait.nom+". \n Il vous reste "+str(client.seance)+" Séances, valables jusqu'au:"+str(client.date_fin.strftime('%d %B %Y'))
    print(Text)

    print("please wait...processing")
    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()

def TextSpeak(Text):
    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()
