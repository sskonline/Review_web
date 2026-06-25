from rest_framework import serializers
from screen.models import Movie

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'