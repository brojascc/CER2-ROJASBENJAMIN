from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LogoutView
from django.http import Http404



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.principal, name='principal'),

    path('login/', views.iniciarSesion, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),

    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<int:pk>/', views.detalle_patrimonio, name='detalle_patrimonio'),
]
