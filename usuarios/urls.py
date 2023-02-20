from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),

    path('sair/', auth_views.LogoutView.as_view(), name="logout"),

    path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Alterar senha atual'},
        success_url=reverse_lazy('home')
        ), name="alterar-senha"),
]
