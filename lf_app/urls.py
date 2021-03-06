'''URL / routing definition for the `loc` application.'''

from django.urls import path

from . import views

app_name = 'lf'

urlpatterns = [
    path('', views.LinkIndexView.as_view(), name='index'),

    path('link/<int:pk>/', views.LinkDetailView.as_view(), name='link'),
    path('links/tagged/<str:tag>/', views.TaggedLinksView.as_view(), name='links_tagged'),
    path('link/create/', views.LinkCreateView.as_view(), name='link_create'),
    path('link/edit/<int:pk>/', views.LinkUpdateView.as_view(), name='link_edit'),
    path('link/delete/<int:pk>/', views.LinkDeleteView.as_view(), name='link_delete'),
    path('link/open/<int:pk>/', views.link_open, name='link_open'),


    path('tags', views.tags_list, name='tags_list'),


    path('search/', views.link_search, name='search'),

    path('find_meta', views.find_metadata, name='find_meta'),

    path('info/', views.info, name='info'),
]
