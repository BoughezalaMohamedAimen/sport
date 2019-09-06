from django.urls import path,include,re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    path('',HomeClient.as_view(),name='home_clients'),
    path('update/<int:id>',UpdateClient.as_view(),name='update_clients'),
    path('get/rfid',csrf_exempt(GetClient.as_view()),name='by_rfid_clients'),
    path('seance/<int:id>',MarquerSeance,name='marquer_seance_clients'),
    path('historique/<int:id>',GetHistorique,name='historique_page_num'),
]
