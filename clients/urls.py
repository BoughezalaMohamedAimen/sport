from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    path('',HomeClient.as_view(),name='home_clients'),
    path('update/<int:id>',UpdateClient.as_view(),name='update_clients'),
]
