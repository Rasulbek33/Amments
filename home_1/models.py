from django.db import models

class Home_1(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    about = models.CharField(max_length=255, blank=True, help_text='Sarlavhaning pasti')
    link = models.URLField(blank=True)
    link_name = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='home_1/images', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    photo_120 = models.ImageField(upload_to='home_1/low_images', blank=True)
    name = models.CharField(max_length=255, blank=True, help_text='Nomi rasmning ')

    photo_432 = models.ImageField(upload_to='home_1/432_image', blank=True)
    about_432 = models.CharField(max_length=255, blank=True, help_text='Rasm haqida')
    price = models.DecimalField(max_digits=6, decimal_places=3)

    photo_big = models.ImageField(upload_to='home_1/big_image', blank=True)
    logo = models.ImageField(upload_to='home_1/logos_image', blank=True)
    date = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Home_1'
        verbose_name_plural = 'Homes_1'


    
class Home_2(models.Model):
    photo_370 = models.ImageField(upload_to='home_2/image', blank=True)
    name = models.CharField(max_length=255, blank=True, help_text='370 rasm nomi')
    main_title = models.CharField(max_length=255, blank=True)
    main_photo = models.ImageField(upload_to='home_2/main_image', blank=True)
    
    main_sub_title = models.CharField(max_length=255, blank=True)
    main_about = models.CharField(max_length=255, blank=True)
    
    photo_432 = models.ImageField(upload_to='home_2/image_432', blank=True)
    about_432 = models.CharField(max_length=255, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=4)
    price = models.DecimalField(max_digits=10, decimal_places=4)

    photo_120 = models.ImageField(upload_to='home_2/image_120', blank=True)
    name_120 = models.CharField(max_length=255, blank=True)
    quantity = models.CharField(max_length=255, blank=True)

    logo = models.ImageField(upload_to='home_2/logo', blank=True)

    date = models.DateField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    news_about = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.main_title
    

    class Meta:
        verbose_name = 'Home_2'
        verbose_name_plural = 'Homes_2'
