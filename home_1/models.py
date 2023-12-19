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


    logo = models.ImageField(upload_to='home_1/logos_image', blank=True)
    date = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Home_1'
        verbose_name_plural = 'Homes_1'


    
