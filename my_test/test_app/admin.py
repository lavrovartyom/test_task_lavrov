from django.contrib import admin
from .models import Habr


class HabrAdmin(admin.ModelAdmin):
	list_display = ['title', 'date', 'user_name', 'user_link']


admin.site.register(Habr, HabrAdmin)