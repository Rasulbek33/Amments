from django.db import models

class Home_2(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Home_2'
        verbose_name_plural = 'Homes_2'