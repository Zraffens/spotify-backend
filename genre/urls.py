from django.urls import path
from .views import GenreList

urlpatterns = [
    path('', GenreList.as_view()),
]
