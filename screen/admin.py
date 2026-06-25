from django.contrib import admin
from .models import Movie, Review

class MOvieadmin(admin.ModelAdmin):
    list_filter = ('year',)
# Register your models here.
admin.site.register(Movie,MOvieadmin)
admin.site.register(Review)