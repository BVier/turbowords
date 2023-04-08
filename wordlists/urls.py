from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('login', views.startpage, name='login'),
    path('authenticate/', views.login_user, name='authenticate'),
    path('patients', views.patients, name='patients'),
    path('add-patient', views.add_patient, name='add-patient'),
    path('set-patient/<int:patientId>', views.set_patient, name='set-patient'),
    path('index/', views.index, name='index'),
    path('list/<int:id>', views.wordlist, name='wordlist'),
    path('test/<int:id>/<int:success>', views.test, name='test'),
    path('start-test/', views.start_test, name='start-test'),
    path('create-wordlist/', views.create_wordlist, name='create-wordlist'),
    path('edit-wordlist/', views.edit_wordlist, name='edit-wordlist'),
    path('delete-wordlist/', views.delete_wordlist, name='delete-wordlist'),
    path('create-wordlist', views.add_wordlist, name='create-wordlist'),
    path('edit-list/<int:id>', views.save_list, name='edit-list'),
]