from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artist_collective_ink_serverapi.models import Style

class StyleView(ViewSet):
  
  def retrieve(self, request, pk):
    style = Style.objects.get(pk=pk)
    serializer = StyleSerializer(style)
    return Response(serializer.data)
  
  def list(self, request):
      styles = Style.objects.all()
      serializer = StyleSerializer(styles, many = True)
      return Response(serializer.data)
    
  def create(self, request):
      style = Style.objects.create(
          name = request.data["name"]
      )
      serializer = StyleSerializer(style)
      return Response(serializer.data)
    
  def update(self, request, pk):
      style = Style.objects.get(pk=pk)
      style.name = request.data["name"]
      style.save()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  def destroy(self, request, pk):
      style = Style.objects.get(pk=pk)
      style.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class StyleSerializer(serializers.ModelSerializer):
  
  class Meta:
      model = Style
      fields = ('name', 'id', 'uid')
      depth = 1
