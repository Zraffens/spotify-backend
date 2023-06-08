from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework import mixins
from rest_framework import generics


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArtistSearchList(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        title = self.kwargs['title'].lower()
        return Artist.objects.filter(title__contains=title)