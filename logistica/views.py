
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomPasswordChangeForm, ConfirmPasswordForm
from django.contrib import messages


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def user_login(request):
    error = None  # Inicialize a variável de erro como None
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    error = 'Sua conta está desativada. Entre em contato com o administrador.'
            else:
                error = 'Usuário ou senha incorretos'
        else:
            # Use form.errors para acessar mensagens de erro específicas dos campos
            error = 'Por favor, corrija os erros no formulário.'
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form, 'error': error})


@login_required
def sair(request):
    logout(request)
    return redirect('login')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Atualiza a sessão de autenticação
            messages.success(request, 'Sua senha foi alterada com sucesso. Faça o login com sua nova senha.')
            return redirect('login')  # Redireciona o usuário para a página de login com a mensagem de sucesso
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')  # Exibe mensagem de erro se o formulário não for válido
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'alterar_senha.html', {'form': form})