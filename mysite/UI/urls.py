from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.company, name='company'),
    path('test/', views.test, name='test'),
    path('model/', views.model, name='model'),
    path('label/', views.label, name='label'),
    path('model2/', views.model2, name='model2'),

]
