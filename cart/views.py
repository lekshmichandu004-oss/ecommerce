from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cart = Cart.objects.get(User=request.user)
        products = Product.objects.get(id=product_id)

        item,created = CartItem.objects.get_or_create(cart=cart, product=products)
        if not created:
            item.quantity += int(quantity)
        else:
            item.quantity = int(quantity)

        item.save()

        return Response({"message": "Item added to cart"})

class UpdateCartItemView(APIView):
        permission_classes = [IsAuthenticated]

        def post(self,request):
            item_id = request.data.get('item_id')
            quantity = request.data.get('quantity')

            item = CartItem.objects.get(id=item_id, cart_User=request.user)
            item.quantity = int(quantity)
            item.save()

            return Response({"message": "Cart updated"})
class RemoveCartItemView(APIView):
        permission_classes = [IsAuthenticated]

        def post(self,request):
            item_id = request.data.get('item_id')

            item = CartItem.objects.get(id=item_id, cart_user=request.user)
            item.delete()
            return Response({"message": "Item removed from cart"})

    
        