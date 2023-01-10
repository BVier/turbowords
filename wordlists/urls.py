from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<int:id>', views.wordlist, name="wordlist"),
    path('start/<int:wordlist>/<str:participant>', views.start_test, name="start"),
    path('test/<int:id>/<int:success>', views.test, name="test"),
]