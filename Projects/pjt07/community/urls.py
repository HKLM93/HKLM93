from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<review_pk>/', views.detail, name='detail'),
    path('<review_pk>/comments/create/', views.comments_create, name='comments_create'),
    path('<review_pk>/like/', views.like, name='like'),
]
