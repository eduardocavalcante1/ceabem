from django.urls import path
from .views.usuario_views import (login_usuario, logout_usuario, home)
from .views.participante_views import (participante)

urlpatterns = [
    path('', login_usuario, name='login_usuario'),
    path('', logout_usuario, name='logout_usuario'),
    path('home', home, name='home'),
    path('participante', participante, name='participante'),
]
