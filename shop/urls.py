from django.urls import path
from shop import views


app_name = 'shop'



urlpatterns = [
    path('Grid_sidebar/', views.Grid_sidebar.as_view(), name='Grid_sidebar'),
    path('Full_with/', views.Full_with.as_view(), name='Full_with'),
    path('List_sidebar/', views.List_sidebar.as_view(), name='List_sidebar'),
    path('Cart/', views.Cart.as_view(), name='Cart'),
    path('wishlist/', views.Wishlist.as_view(), name='wishlist'),
    path('compare/', views.Compare.as_view(), name='compare'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('login/', views.Login.as_view(), name='login')

]

