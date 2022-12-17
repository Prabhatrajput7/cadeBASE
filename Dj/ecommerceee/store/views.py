from django.shortcuts import render
from store.models import Product
from cart.models import Cart,CartItem
from cart.views import _get_product_session_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def storefx(request,slugcat=None):

    if slugcat:
        productslg = Product.objects.select_related('category').filter(category__slug =slugcat).order_by('-id')
        paginator = Paginator(productslg,1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        context={
            'product':paged_product,
            'p_count':productslg.count()
        }
        return render(request,'store/store.html',context)
    product = Product.objects.filter(is_available =True).order_by('-id')
    # print('product', product)
    paginator = Paginator(product,3)
    # print('paginator', paginator)
    page = request.GET.get('page')
    # print('page',page)
    paged_product = paginator.get_page(page)
    # print('pp',paged_product)
    context = {
        'product':paged_product,
        'p_count':product.count()
    }
    return render(request,'store/store.html',context)


def productdetfx(request,slugcat,slugpro):
    try:
        productdetailslg = Product.objects.select_related('category').get(category__slug =slugcat,slug=slugpro)
        is_in_cart = CartItem.objects.filter(product=productdetailslg, cart__cart_id = _get_product_session_id(request)).exists()
    except Exception as e:
        raise e
    context = {
        'productdetail':productdetailslg,
        'in_cart': is_in_cart
    }
    return render(request,'store/pdetail.html',context)

def searching(request):
    # print(request.GET) <QueryDict: {'keyword': ['hell']}>
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        else:
            products = Product.objects.filter(is_available =True).order_by('-id')
            product_count = products.count()
            """
            products = False
            product_count = 0
            """
    context = {
        'product': products,
        'p_count': product_count,
    }
    return render(request, 'store/store.html', context)    