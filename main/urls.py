from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve/<int:tool_id>/', views.reserve, name='reserve'),
]