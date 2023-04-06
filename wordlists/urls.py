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
    path('create-wordlist/', views.create_wordlist, name='create-wordlist'),
    path('edit-wordlist/<int:id>', views.edit_wordlist, name='edit-wordlist'),
    path('delete-wordlist/<int:id>', views.delete_wordlist, name='delete-wordlist'),
    path('save-new-list', views.save_new_list, name='save-new-list'),
    path('save-list/<int:id>', views.save_list, name='save-list'),
]