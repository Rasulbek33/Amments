from django.contrib import admin
from home_1.models import Home_2

@admin.register(Home_2)
class Home_2(admin.ModelAdmin):
    list_display = ('main_title', 'quantity', 'date')
    list_display_links = ('main_title', 'quantity', )
    list_filter = ('date',)
