from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultation', views.consultation, name='consultation'),
    path('materiel', views.materiel, name='materiel'),
    path('sortie', views.sortie, name='sortie'),
    path('retour', views.retour, name='retour'),
    path('pret', views.pret, name='pret'),
    path('recherche', views.recherche, name='recherche'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('tool_feed', views.tool_feed, name='tool_feed'),
    path('reserve/<int:tool_id>/', views.reserve, name='reserve'),
]