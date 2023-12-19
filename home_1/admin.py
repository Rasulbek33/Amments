from django.contrib import admin
from home_1.models import Home_1

@admin.register(Home_1)
class Home_1(admin.ModelAdmin):
    list_display = ('title', 'name', 'photo',)
    list_display_links = ('title', 'photo', 'name',)
    list_filter = ('price',)


