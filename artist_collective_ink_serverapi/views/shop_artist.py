
# from django.db import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from artist_collective_ink_serverapi.models import Shop, Artist, Shop_Artist

# class ShopArtistView(ViewSet):

#   def create(self, request):
    
#     artist = Artist.objects.get(request.data["artist_id"])
#     shop = Shop.objects.get(pk=request.datas["shop_id"])
    
#     shop_artist = Shop_Artist.objects.create(
#       artist = artist,
#       shop = shop
#     )
    
#     serializer = ShopArtistSerializer(shop_artist)
#     return Response(serializer.data)
  
#   def destroy (self, request, pk):
#     shop_artist = Shop_Artist.objects.get(pk=pk)
#     shop_artist.delete()
    
#     return Response(None, status=status.HTTP_204_NO_CONTENT)
  
# class ShopArtistSerializer(serializers.ModelSerializer):
    
#     class Meta:
#       model = Shop_Artist
#       fields = ('id', 'artist', 'shop')
#       depth = 1
