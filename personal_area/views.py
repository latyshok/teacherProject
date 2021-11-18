from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import TemplateView

from personal_area.forms import AuthForm


class AuthView(View):
    def post(self, request):
        form = AuthForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('email'),
                                password=form.cleaned_data.get('password'))

            if user:
                login(request, user)
                return redirect('admin:index')
            else:
                form.add_error('password', 'Не существует такой пары email/password')

        return render(request, 'personal_area/auth.html', context={
            'form': form
        })

    def get(self, request):
        return render(request, 'personal_area/auth.html', context={
            'form': AuthForm()
        })
