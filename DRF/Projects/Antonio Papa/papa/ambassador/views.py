from cProfile import label
import math, random, time, string

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import User
from common.authjwt import JWTauth
from common.serializers import UserSerializer
from .serializers import ProductSerializer, LinkSerializer
from app.models import Product, Link, Order, User
from django.core.cache import cache


class ProductFrontendAPIView(APIView):
    @method_decorator(cache_page(60 * 60 * 2, key_prefix='products_frontend'))
    def get(self, _):
        time.sleep(2)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductBackendAPIView(APIView):

    def get(self, request):
        products = cache.get('products_backend')
        if not products:
            time.sleep(2)
            products = list(Product.objects.all())
            cache.set('products_backend', products, timeout=60 * 30)  # 30 min
        
        s = request.query_params.get('s', '')
        if s:
            products = list([
                p for p in products
                if (s.lower() in p.title.lower()) or (s.lower() in p.description.lower())
            ])

        sort = request.query_params.get('sort', None)

        if sort == 'asc':
            products.sort(key=lambda p: p.price)
        elif sort == 'desc':
            products.sort(key=lambda p: p.price, reverse=True)

        per_page = 9
        page = int(request.query_params.get('page', 1))
        start = (page - 1) * per_page
        end = page * per_page

        total = len(products)

        data = ProductSerializer(products[start:end], many=True).data
        return Response({
            'data': data,
            'meta': {
                'total': total,
                'page': page,
                'last_page': math.ceil(total / per_page)
            }
        })


class LinkAPIView(APIView):
    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        serializer = LinkSerializer(data={
            'user': user.id,
            'code': ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)),
            'products': request.data['products']
        })
        """
        products = {[2,4]}
        """
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class StatsAPIView(APIView):
    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        links = Link.objects.filter(user_id=user.id)

        return Response([self.format(link) for link in links])

    def format(self, link):
        orders = Order.objects.filter(code=link.code, complete=1)

        return {
            'code': link.code,
            'count': len(orders),
            'revenue': sum(o.ambassador_revenue for o in orders)
        }


class RankingsAPIView(APIView):
    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = User.objects.filter(is_ambassador = True)
        # response = list({
        #     'name': a.name,
        #     "revenue":a.revenue
        # } for a in user)

        # response.sort(key = lambda x:x['revenue'], reverse=True)
        # return Response(response)
        con = get_redis_connection("default")

        rankings = con.zrevrangebyscore('rankings', min=0, max=10000, withscores=True)
        print(rankings)
# [(b'ad None', 100.0), (b'z None', 5.0), (b'f None', 0.0), (b'Tyler Patterson', 0.0), (b'Tara Brown', 0.0), (b'Stephanie Benson', 0.0), (b'Shawna Graham', 0.0), (b'Ryan Wood', 0.0), (b'Ruth Logan', 0.0), (b'Robert Palmer', 0.0), (b'Patrick Sellers', 0.0), (b'None None', 0.0), (b'Michael Morgan', 0.0), (b'Michael James', 0.0), (b'Marcus Ortiz', 0.0), (b'Lawrence Fuller', 0.0), (b'Kristin Carroll', 0.0), (b'Kristie Short', 0.0), (b'Julie Gould', 0.0), (b'Juan Robertson', 0.0), (b'Jeffery Moore', 0.0), (b'Hannah Walker', 0.0), (b'Gregory Baker', 0.0), (b'Douglas Mann', 0.0), (b'David Cook', 0.0), (b'Cynthia Pittman', 0.0), (b'Christina Ruiz', 0.0), (b'Cassandra Fuller', 0.0), (b'Aaron Knox', 0.0), (b' ', 0.0)]

        return Response({
            r[0].decode("utf-8"): r[1] for r in rankings
        })