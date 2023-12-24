from django.contrib import admin
from shop.models import Grid_sidebar, Full_with, List_sidebar, Cart, Wishlist, Compare, Checkout, Product_detail, Product_group, Product_slider

@admin.register(Grid_sidebar)
class Grid_sidebar(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'photo_sub_title',)
    list_display_links = ('title', 'sub_title',)

@admin.register(Full_with)
class Full_with(admin.ModelAdmin):
    list_display = ('title', 'photo_sub_title',)
    list_display_links = ('title',)


@admin.register(List_sidebar)
class List_sidebar(admin.ModelAdmin):
    list_display = ('title', 'photo_title',)
    list_display_links = ('title', 'photo_title',)


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)

@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)

@admin.register(Compare)
class Compare(admin.ModelAdmin):
    list_display = ('title',  'photo_title', 'description', 'color',)
    list_display_links = ('title', 'photo_title', 'description', )


@admin.register(Checkout)
class Checkout(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)


@admin.register(Product_detail)
class Product_detail(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price', 'photo_sub_title', 'text_title', 'text_sub_title',)
    list_display_links = ('title', 'sub_title', 'text_title',)


@admin.register(Product_group)
class Product_group(admin.ModelAdmin):
    list_display = ('photo_title', 'photo_sub_title', 'price', 'photo_1_about',)
    list_display_links = ('photo_title', 'photo_sub_title', 'photo_1_about',)


@admin.register(Product_slider)
class Product_slider(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price', 'photo_sub_title',)
    list_display_links = ('title', 'sub_title',)