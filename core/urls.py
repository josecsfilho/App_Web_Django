
from django.contrib import admin
from django.urls import path
from logistica import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.user_login, name='login'),
    path("home/", views.home, name='home'),
    path("sair/", views.sair, name='sair'),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),

]
