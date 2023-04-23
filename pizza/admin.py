from django.contrib import admin

from .models import Pizza, Orders, Seller, Day

admin.site.register(Pizza)
admin.site.register(Orders)
admin.site.register(Seller)
admin.site.register(Day)

