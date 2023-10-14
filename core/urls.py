
from django.contrib import admin
from django.urls import path, include
from logistica import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", views.user_login, name='login'),
    path("", views.home, name='home'),
    path("sair/", views.sair, name='sair'),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
]
