from rest_framework import generics,viewsets
from .serializers import Movieserializer
from screen.models import Movie
from screen.api.filters import MovieFilter
class Movielist(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movieserializer
    filterset_class = MovieFilter