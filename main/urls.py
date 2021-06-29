from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultation', views.consultation, name='consultation'),
    path('materiel', views.materiel, name='materiel'),
    path('sortie', views.sortie, name='sortie'),
    path('retour', views.retour, name='retour'),
    path('pret', views.pret, name='pret'),
    path('reserve/<int:tool_id>/', views.reserve, name='reserve'),
]