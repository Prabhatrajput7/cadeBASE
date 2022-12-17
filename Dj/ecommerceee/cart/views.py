from tkinter.messagebox import NO
from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product, Variation
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def _get_product_session_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 

def cartfx(request, total=0, quantity=0, cartitems=None,tax =None,grandtotal=None):
    try:
        if request.user.is_authenticated:
            cartitems = CartItem.objects.filter(user= request.user,is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_get_product_session_id(request))
            cartitems = CartItem.objects.filter(cart=cart,is_active=True)
        # cartitems = CartItem.objects.filter(cart=cart,is_active=True)
        for cartitem in cartitems:
            total += (cartitem.product.price * cartitem.quantity)
            quantity += cartitem.quantity
        tax = (2 * total)/100
        grandtotal = total + tax
    except ObjectDoesNotExist:
        pass #just ignore
    context = {
        'total': total,
        'quantity': quantity,
        'cartitems': cartitems,
        'tax'       : tax,
        'grandtotal': grandtotal,
    }

    return render(request,'cart/cart.html',context)
   

def addtocart(request,id):
    current_user = request.user
    product = Product.objects.get(id=id)
    lst =[]
    if current_user.is_authenticated:
        if request.method == "POST":
            # print(request.POST)
            # <QueryDict: {'csrfmiddlewaretoken': ['soUSWUsid5rXHrun5D7dZmX4lLNanmwnVcCqfbUDZr8a92xxypEMRV1ECaU6jULA'], 'color': ['Green'], 'size': ['M']}>
            for r in request.POST:
                key = r
                value = request.POST[key]
                try:    
                    variation = Variation.objects.get(product= product,variation_category__iexact= key,variation_value__iexact=value)
                    lst.append(variation)
                except:
                    pass

        is_cart_item_ex = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_ex:
            cartget = CartItem.objects.filter(product=product, user=current_user)
            ex_cari,ids = [],[]
            for item in cartget:
                ex = item.variation.all()
                ex_cari.append(list(ex))
                ids.append(item.id)
            # withos adding list(ex) [<QuerySet [<Variation: Red>, <Variation: S>]>]
            # with list [[<Variation: Red>, <Variation: S>]]

            if lst in ex_cari:
                index= ex_cari.index(lst)
                Id = ids[index]
                cartItem = CartItem.objects.get(product=product,id =Id)
                cartItem.quantity += 1
                cartItem.save()

            else:
                cartItem = CartItem.objects.create(product=product,user=current_user,quantity = 1)
                if len(lst)>0:
                    cartItem.variation.clear()
                    cartItem.variation.add(*lst)
                cartItem.save()
        else:
            cartitem = CartItem.objects.create(product = product,user=current_user,quantity = 1)
            if len(lst)>0:
                cartitem.variation.clear()
                cartitem.variation.add(*lst)
            cartitem.save()

        return redirect('cart:cartfx')

# id user is not authenticated
    else:
        lst = []
        if request.method == "POST":
            for r in request.POST:
                # <QueryDict: {'csrfmiddlewaretoken': ['soUSWUsid5rXHrun5D7dZmX4lLNanmwnVcCqfbUDZr8a92xxypEMRV1ECaU6jULA'], 'color': ['Green'], 'size': ['M']}>
                key = r
                value = request.POST[key]
                try:    
                    variation = Variation.objects.get(product= product,variation_category__iexact= key,variation_value__iexact=value)
                    if variation:
                        lst.append(variation)
                except:
                    pass
        # print(lst) [<Variation: Red>, <Variation: XL>] color and size
        try:
            cart = Cart.objects.get(cart_id=_get_product_session_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_get_product_session_id(request))
        

        is_cart_item_ex = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_ex:
            cartget = CartItem.objects.filter(product=product, cart=cart)
            # print(cartget)
            #exiting variation
            # new variation
            # id
            ex_cari,ids = [],[]
            for item in cartget:
                ex = item.variation.all()
                # print(ex)
                ex_cari.append(list(ex))
                ids.append(item.id)
            # withos adding list(ex) [<QuerySet [<Variation: Red>, <Variation: S>]>]
            # with list [[<Variation: Red>, <Variation: S>]]

            if lst in ex_cari:
                index= ex_cari.index(lst)
                Id = ids[index]
                cartItem = CartItem.objects.get(product=product,id =Id)
                cartItem.quantity += 1
                cartItem.save()

            else:
                cartItem = CartItem.objects.create(product=product,cart= cart,quantity = 1)
                if len(lst)>0:
                    cartItem.variation.clear()
                    cartItem.variation.add(*lst)
                cartItem.save()
        else:
            cartitem = CartItem.objects.create(product = product,cart=cart,quantity = 1)
            if len(lst)>0:
                cartitem.variation.clear()
                cartitem.variation.add(*lst)
            cartitem.save()

        return redirect('cart:cartfx')

        

    # try:
    #     cartget = CartItem.objects.get(product=product, cart=cart)
    #     cartget.quantity +=1
    #     print('noo')
    #     if len(lst)>1:
    #         print('no')
    #         cartget.variation.clear()
    #         for ls in lst:
    #             cartget.variation.add(ls)
    #     cartget.save()
    # except:
    #     cartitem = CartItem.objects.create(product = product,cart=cart,quantity = 1)
    #     if len(lst)>1:
    #         cartitem.variation.clear()
    #         for ls in lst:
    #             cartitem.variation.add(ls)
    #     cartitem.save()
    # return redirect('cart:cartfx')   

def decrementfromcart(request,id,cart_id):
    product = get_object_or_404(Product, id=id)
    if request.user.is_authenticated:
        cartitem = CartItem.objects.get(product=product, user=request.user, id=cart_id)
    else:
        cart = Cart.objects.get(cart_id=_get_product_session_id(request))
        cartitem = CartItem.objects.get(product=product, cart=cart, id=cart_id)
   
    if cartitem.quantity > 1:
        cartitem.quantity -= 1
        cartitem.save()
    else:
        cartitem.delete()


    return redirect('cart:cartfx')    

def removefromcart(request,id,cart_id):
    product = get_object_or_404(Product, id=id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_id)
    else:
        cart = Cart.objects.get(cart_id=_get_product_session_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_id)
    cart_item.delete()
    return redirect('cart:cartfx')  
         

@login_required(login_url = 'user:login')     
def checkout(request,total=0, quantity=0, cartitems=None,tax =None,grandtotal=None):
    try:
        if request.user.is_authenticated:
            cartitems = CartItem.objects.filter(user= request.user,is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_get_product_session_id(request))
            cartitems = CartItem.objects.filter(cart=cart,is_active=True)
        for cartitem in cartitems:
            total += (cartitem.product.price * cartitem.quantity)
            quantity += cartitem.quantity
        tax = (2 * total)/100
        grandtotal = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cartitems': cartitems,
        'tax'       : tax,
        'grandtotal': grandtotal,
    }

    return render(request,'cart/checkout.html',context)    