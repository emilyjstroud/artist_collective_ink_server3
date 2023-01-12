from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artist_collective_ink_serverapi.models import ArtistStyle, Artist, Style

class ArtistStyleView(ViewSet):
  
  def retrieve(self, request, pk):
      artist_style = ArtistStyle.objects.get(pk=pk)
      serializer = ArtistStyleSerializer(artist_style)
      return Response(serializer.data)
  
  def list(self, request):
      artist_styles = ArtistStyle.objects.all()
      serializer = ArtistStyleSerializer(artist_styles, many = True)
      return Response(serializer.data)
    
  def create(self, request):
      artist = Artist.objects.get(pk=request.data["artist"])
      style = Style.objects.get(pk=request.data["style"])
      
      artist_style = ArtistStyle.objects.create(
        artist = artist,
        style = style
      )
      serializer = ArtistStyleSerializer(artist_style)
      return Response(serializer.data)
    
  def update(self, request, pk):
      artist_style = ArtistStyle.objects.get(pk=pk)
      
      artist = Artist.objects.get(pk=request.data["artist"])
      style = Style.objects.get(pk=request.data["style"])
      
      artist_style.artist = artist
      artist_style.style = style
      artist_style.save()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  def destroy(self, request, pk):
      artist_style = ArtistStyle.objects.get(pk=pk)
      artist_style.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ArtistStyleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = ArtistStyle
    fields = ('artistId', 'styleId', 'id')
    depth = 1
