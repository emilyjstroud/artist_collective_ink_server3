from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artist_collective_ink_serverapi.models import Shop, User

class ShopView(ViewSet):
  
  def retrieve(self, request, pk):
    
      shop = Shop.objects.get(pk=pk)
      serializer = ShopSerializer(shop)
      return Response(serializer.data)
    
  def list(self, request):
    
      shops = Shop.objects.all()
      
      uid_query = request.query_params.get('uid', None)
      if uid_query is not None:
        shops = shops.filter(user=uid_query)
      serializer = ShopSerializer(shops, many = True)
      return Response(serializer.data)
    
  def create(self, request):
    
    user = User.objects.get(uid=request.data["user"])
    
    shop = Shop.objects.create(
      name = request.data["name"],
      location = request.data["location"],
      website = request.data["website"],
      photo = request.data["photo"],
    )
    serializer = ShopSerializer(shop)
    return Response(serializer.data)
  
  def update(self, request, pk):
    
    shop = Shop.objects.get(pk=pk)
    
    shop.name = request.data["name"]
    shop.location = request.data["location"]
    shop.website = request.data["website"]
    shop.photo = request.data["photo"]
    shop.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      shop = Shop.objects.get(pk=pk)
      shop.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ShopSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Shop
    fields = ('name', 'location', 'website', 'photo', 'id', 'user')
    depth = 1
