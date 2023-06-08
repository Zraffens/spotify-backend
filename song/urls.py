from django.urls import path
from .views import SongList, SongDetail, SongSearchList, LikedList

urlpatterns = [
    path('', SongList.as_view()),
    path('liked/', LikedList.as_view()),
    path('<int:pk>/', SongDetail.as_view()),
    path('filter/<str:title>/', SongSearchList.as_view()),
]
