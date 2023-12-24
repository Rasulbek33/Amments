from django.db import models

class Grid_sidebar(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='grid_sidebar/images', blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Grid_sidebar'
        verbose_name_plural = 'Grid_sidebars'


class Full_with(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='full_with/images', blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3)



    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Full_with'
        verbose_name_plural = 'Full_withs'


class List_sidebar(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='List_sidebar/images', blank=True)
    photo_title = models.CharField(max_length=255 ,blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title 
    

    class Meta:
        verbose_name = 'List_sidebar'
        verbose_name_plural = 'List_sidebars'


class Cart(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Cart/images', blank=True)
    photo_name = models.CharField(max_length=255, blank=True)
    photo_price = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'



class Wishlist(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Wishlist/images', blank=True)
    photo_name = models.CharField(max_length=255, blank=True)
    photo_price = models.DecimalField(max_digits=6, decimal_places=3)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    
class Compare(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Compare/images', blank=True)
    photo_title = models.CharField(max_length=255, blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    color = models.CharField(max_length=50, blank=True)

    


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



class Product_detail(models.Model):
    photo = models.ImageField(upload_to='product_detail/images')
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    photo_123 = models.ImageField(upload_to='product_detail/photo_123', blank=True)
    text_title = models.CharField(max_length=255, blank=True)
    text_sub_title = models.CharField(max_length=255, blank=True)
    photo_432 = models.ImageField(upload_to='product_detail/photo_432', blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)
    price_432 = models.DecimalField(max_digits=6, decimal_places=3)
    photo_3 = models.ImageField(upload_to='product_detail/photo_3', blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Product_detail'
        verbose_name_plural = 'Product_details'


class Product_group(models.Model):
    photo = models.ImageField(upload_to='product_group/images', blank=True)
    photo_title = models.CharField(max_length=255, blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    photo_1 = models.ImageField(upload_to='product_group/photo_1', blank=True)
    photo_1_about = models.CharField(max_length=255, blank=True)
    photo_2 = models.ImageField(upload_to='product_group/photo_2', blank=True)

    def __str__(self) -> str:
        return self.photo_title
    
    class Meta:
        verbose_name = 'Product_group'
        verbose_name_plural = 'Product_groups'


class Product_slider(models.Model):
    photo = models.ImageField(upload_to='product_slider/images', blank=True)
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    photo_1 = models.ImageField(upload_to='product_slider/photo_1', blank=True)
    photo_sub_title = models.CharField(max_length=255, blank=True)
    photo_2 = models.ImageField(upload_to='product_slider/photo_2', blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Product_slider'
        verbose_name_plural = 'Product_sliders'


class Product_tab(models.Model):
    photo = models.ImageField(upload_to='product_tab/images', blank=True)
    