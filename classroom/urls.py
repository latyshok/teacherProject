from django.urls import path

from classroom.views import IndexView

app_name = 'classroom'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
