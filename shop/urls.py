from django.urls import path
from shop import views


app_name = 'shop'



urlpatterns = [
    path('Grid_sidebar/', views.grid_sidebar, name='grid_sidebar'),
    path('Full_with/', views.full_with, name='Full_with'),
    path('List_sidebar/', views.list_sidebar, name='List_sidebar'),
    path('Cart/', views.cart, name='Cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('compare/', views.compare, name='compare'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('login/', views.Login.as_view(), name='login'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('product_group/', views.product_group, name='product_group'),
    path('product_slider/', views.product_slider, name='product_slider')

]

