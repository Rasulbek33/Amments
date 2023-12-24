from django.shortcuts import render
from shop.models import Grid_sidebar, Full_with, List_sidebar, Cart, Wishlist, Compare, Checkout, Login, My_account, Product_detail, Product_group, Product_slider
from django.views.generic import ListView
from django.utils.translation import gettext as _


def grid_sidebar(request):
    grid_sidebar = Grid_sidebar.objects.all()
    context = {'grid_sidebar':grid_sidebar}
    return render(request, 'shop_grid_sidebar.html', context)


def full_with(request):
    full_with = Full_with.objects.all()
    context = {'full_with':full_with}
    return render(request, 'shop_full_width.html', context)

def list_sidebar(request):
    list_sidebar = List_sidebar.objects.all()
    context = {'list_sidebar':list_sidebar}
    return render(request, 'shop_list_sidebar.html', context)

def cart(request):
    cart = Cart.objects.all()
    context = {'cart':cart}
    return render(request, 'cart.html', context)


def wishlist(request):
    wishlist = Wishlist.objects.all()
    context = {'wishlist':wishlist}
    return render(request, 'wishlist.html', context)

def compare(request):
    compare = Compare.objects.all()
    context = {'compare':compare}
    return render(request, 'compare.html', context)

class Checkout(ListView):
    model = Checkout
    template_name = 'checkout.html'

class Login(ListView):
    model = Login
    template_name = 'login.html'

class My_account(ListView):
    model = My_account
    template_name = 'may_account.html'


def product_detail(request):
    produc_detail = Product_detail.objects.all()
    context = {'product_detail':produc_detail}
    return render(request, 'product-details-default.html', context)


def product_group(request):
    product_group = Product_group.objects.all()
    context = {'product_group':product_group}
    return render(request, 'product-details-group.html', context)


def product_slider(request):
    product_slider = Product_slider.objects.all()
    context = {'product_slider':product_slider}
    return render(request, 'product-details-single-slide.html', context)
