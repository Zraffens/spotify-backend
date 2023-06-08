from django.urls import path
from .views import ArtistList, ArtistDetail, ArtistSearchList

urlpatterns = [
    path('', ArtistList.as_view()),
    path('<int:pk>/', ArtistDetail.as_view()),
    path('filter/<str:title>/', ArtistSearchList.as_view()),
]
