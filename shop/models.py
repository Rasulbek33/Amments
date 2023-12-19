from django.db import models

class Grid_sidebar(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Grid_sidebar'
        verbose_name_plural = 'Grid_sidebars'


class Full_with(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Full_with'
        verbose_name_plural = 'Full_withs'


class List_sidebar(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title 
    

    class Meta:
        verbose_name = 'List_sidebar'
        verbose_name_plural = 'List_sidebars'


class Cart(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'



class Wishlist(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    
class Compare(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Compare'
        verbose_name_plural = 'Compares'


class Checkout(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'



class Login(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'

    
class My_account(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'My_account'
        verbose_name_plural = 'My_accounts'