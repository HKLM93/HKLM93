from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('actors/', views.get_actor_all),
    path('actors/<int:actor_pk>/', views.get_actor_detail),
    path('movies/', views.get_movie_all),
    path('movies/<int:movie_pk>/', views.get_movie_detail),
    path('movies/<int:movie_pk>/review/', views.get_review_all),
    path('movies/review/<int:review_pk>/', views.get_review_detail),
    path('staff/', views.get_staff_all),
    path('staff/<int:staff_pk>/', views.get_staff_detail),
]