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
    
    """ More info needs to go here """
    
    artist = Artist.objects.create(
      """ And here """
    )
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

  def update(self, request, pk):
    artist = Artist.objects.get(pk=pk)
    
    """ More info needs to go here """
    
    artist.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      artist = Artist.objects.get(pk=pk)
      artist.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ArtistSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Artist
    fields = ('name', 'instagram', 'artworkPhoto', 'shopId', 'styleId', 'id', 'uid')
    depth = 1
