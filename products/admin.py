from django.contrib import admin
from .models import Products,Review,Tag

# Register your models here.
admin.site.register(Products)
admin.site.register(Tag)
admin.site.register(Review)

