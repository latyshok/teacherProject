from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View


class BaseRoomView(LoginRequiredMixin, View):
    login_url = '/login'


class IndexView(BaseRoomView):

    def get(self, request):
        user: User = request.user

        is_teacher = user.groups.filter(name='Teachers').exists()
        is_student = user.groups.filter(name='Students').exists()
        print('is_teacher', is_teacher)
        print('is_student', is_student)
        print('is_has_perm', user.has_perm('classroom.access_lk'))

        return render(request, 'classroom/index.html', context={})
