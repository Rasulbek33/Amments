from django.shortcuts import render
from shop.models import Grid_sidebar, Full_with, List_sidebar, Cart, Wishlist, Compare, Checkout, Login, My_account
from django.views.generic import ListView
from django.utils.translation import gettext as _


class Grid_sidebar(ListView):
    model = Grid_sidebar
    template_name = 'shop_grid_sidebar.html'


class Full_with(ListView):
    model = Full_with
    template_name = 'shop_full_width.html'

class List_sidebar(ListView):
    model = List_sidebar
    template_name = 'shop_list_sidebar.html'

class Cart(ListView):
    model = Cart
    template_name = 'cart.html'


class Wishlist(ListView):
    model = Wishlist
    template_name = 'wishlist.html'

class Compare(ListView):
    model = Compare
    template_name = 'compare.html'

class Checkout(ListView):
    model = Checkout
    template_name = 'checkout.html'

class Login(ListView):
    model = Login
    template_name = 'login.html'

class My_account(ListView):
    model = My_account
    template_name = 'may-account.html'
