from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artist_collective_ink_serverapi.models import Artist

class ArtistView(ViewSet):
  
  def retrieve(self, request, pk):
    artist = Artist.objects.get(pk=pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)
  
  def list(self, request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    artist = Artist.objects.create(
      name = request.data["name"],
      instagram = request.data["instagram"],
      artworkPhoto = request.data["artworkPhoto"],
      shop = request.data["shop"],
      style = request.data["style"],
      id = request.data["id"]
    )
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

  def update(self, request, pk):
    artist = Artist.objects.get(pk=pk)
    artist.name = request.data["name"]
    artist.instagram = request.data["instagram"]
    artist.artworkPhoto = request.data["artworkPhoto"]
    artist.shop= request.data["shop"]
    artist.style= request.data["style"]
    artist.id = request.data["id"]
    
    artist.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      artist = Artist.objects.get(pk=pk)
      artist.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ArtistSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Artist
    fields = ('name', 'instagram', 'artworkPhoto', 'shop', 'style', 'id')
    depth = 1
