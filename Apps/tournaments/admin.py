from django.contrib import admin

from .models import Tournament, Point, Interclub
# Register your models here.
admin.site.register(Tournament)
admin.site.register(Point)
admin.site.register(Interclub)