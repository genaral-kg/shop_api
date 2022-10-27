from django.contrib import admin

# Register your models here.

from rating.models import Review

admin.site.register(Review)