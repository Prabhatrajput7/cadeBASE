
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("productsdeflist/", views.product_list, name="product-list-fx"),
    path("productsdefdet/<int:pk>/", views.product_detail, name="product-details-fx"),
    path("products/<int:pk>/", views.ProductDetails.as_view(), name="product-detail"),
    # mANUFACTURE
    path("manu/", views.ManuList.as_view(), name="manufacturer-list"),
    path("manu/<int:pk>/", views.ManuDetails.as_view(), name="manufacturer-detail"),
    path("manudeflist/", views.manu_list, name="manu-details-def"),
    path("manudefdet/<int:pk>/", views.manu_detail, name="manu-detail-def"),
    
]