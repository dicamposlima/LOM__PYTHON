from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.view, name='view'),
    path('search/', views.search, name='search'),
]
