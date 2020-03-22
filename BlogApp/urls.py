from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<int:BlogApp_id>/', views.detail, name='detail'),
]
