from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artist_collective_ink_serverapi.models import Artist, Shop, Style

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
    
    shop = Shop.objects.get(pk=request.data["shop"])
    style = Style.objects.get(pk=request.data["style"])
    
    artist = Artist.objects.create(
      shop = shop,
      style = style,
      name = request.data["name"],
      location = request.data["location"],
      instagram = request.data["instagram"],
      artworkPhoto = request.data["artworkPhoto"],
    )
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

  def update(self, request, pk):
    artist = Artist.objects.get(pk=pk)
    
    shop = Shop.objects.get(pk=request.data["shop"])
    style = Style.objects.get(pk=request.data["style"])
    
    artist.shop = shop
    artist.style = style
    artist.name = request.data["name"]
    artist.location = request.data["location"]
    artist.instagram = request.data["instagram"]
    artist.artworkPhoto = request.data["artworkPhoto"]
    
    artist.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      artist = Artist.objects.get(pk=pk)
      artist.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ArtistSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Artist
    fields = ('id', 'name', 'location', 'instagram', 'artworkPhoto', 'shop', 'style')
    depth = 1
