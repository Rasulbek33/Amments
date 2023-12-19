from django.contrib import admin
from shop.models import Grid_sidebar, Full_with, List_sidebar, Cart, Wishlist, Compare, Checkout

@admin.register(Grid_sidebar)
class Grid_sidebar(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)

@admin.register(Full_with)
class Full_with(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)


@admin.register(List_sidebar)
class List_sidebar(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)

@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)

@admin.register(Compare)
class Compare(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)


@admin.register(Checkout)
class Checkout(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title',)