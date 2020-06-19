'''URL / routing definition for the `loc` application.'''

from django.urls import path

from . import views

app_name = 'lf'

urlpatterns = [
    path('', views.index, name='index'),

    path('search/', views.search, name='search'),

    path('info/', views.info, name='info'),
]
