from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('login', views.startpage, name='login'),
    path('authenticate/', views.login_user, name='authenticate'),
    path('index/', views.index, name='index'),
    path('list/<int:id>', views.wordlist, name='wordlist'),
    path('start/<int:wordlist>/<str:participant>/<int:duration>', views.start_test, name='start'),
    path('test/<int:id>/<int:success>', views.test, name='test'),
    path('start-test/', views.start_test, name='start-test'),
]