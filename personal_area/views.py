from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import TemplateView

from personal_area.forms import AuthForm


@login_required(login_url='/login')
def index_view(request):
    return redirect('classroom:index')


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('classroom:index')


class AuthView(View):
    def post(self, request):
        form = AuthForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('email'),
                                password=form.cleaned_data.get('password'))

            if user:
                login(request, user)
                return redirect('classroom:index')
            else:
                form.add_error('password', 'Не существует такой пары email/password')

        return render(request, 'personal_area/auth.html', context={
            'form': form
        })

    def get(self, request):
        return render(request, 'personal_area/auth.html', context={
            'form': AuthForm()
        })
