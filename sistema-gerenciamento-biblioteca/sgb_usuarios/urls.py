from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastra_usuario, name='cadastro'),
    path('login/', views.loga_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]
