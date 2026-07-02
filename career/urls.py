from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('questionnaire/', views.questionnaire, name='questionnaire'),

    path('result/', views.result, name='result'),

    path('contact/', views.contact, name='contact'),

]