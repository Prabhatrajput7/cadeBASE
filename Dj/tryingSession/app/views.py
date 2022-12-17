from django.shortcuts import render,redirect
import requests
from .models import Product
# Create your views here.

def index(request):
    product = Product.objects.all()
    context = {'products':product}
    return render(request,'app/index.html',context)

def load_products(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        product = Product(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            image_url=item['image']
        )
        product.save()

    return redirect('index')

def product(request,product_id):
    p = Product.objects.get(pk = product_id)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)
        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        # print(Product.objects.filter(pk__in=[1,2,3]))
        # It means, give me all objects of model Model that either have 1,2 or 3 as their primary key.
        print(products)
        
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id))
        # print(recently_viewed_products) sorting product
        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True
    context = {'product': p, 'recently_viewed_products': recently_viewed_products}
    return render(request,'app/product.html',context)

        