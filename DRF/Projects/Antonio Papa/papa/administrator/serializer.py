from rest_framework import serializers
from app.models import Product, Link, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):

    orders = serializers.SerializerMethodField('get_orders')
    pdetails = serializers.SerializerMethodField('p_d')
    
    def get_orders(self, obj):
        return OrderSerializer(Order.objects.filter(code=obj.code), many=True).data

    def p_d(self,obj):
        l =[]
        items = Link.objects.filter(user_id=obj.user_id)
        for item in items:
            for i in item.products.all():
                l.append(i.title)
        return l

    class Meta:
        model = Link
        fields = '__all__'        

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        items = OrderItem.objects.filter(order_id=obj.id)
        osum = sum((o.price * o.quantity) for o in items)
        return osum

# os x
# is <QuerySet [<OrderItem: X>]>
# o 50.00
# os y
# is <QuerySet [<OrderItem: Y>]>
# o 100.00
# os z
# is <QuerySet [<OrderItem: Z>]>
# o 100.00

    class Meta:
        model = Order
        fields = '__all__'        