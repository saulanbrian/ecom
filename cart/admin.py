from django.contrib import admin

from .models import Cart

class CartAdmin(admin.ModelAdmin):
  class Meta:
    model = Cart
    exclude = ('user')

admin.site.register(Cart,CartAdmin)