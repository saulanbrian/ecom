from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
  class Meta:
    model = Order
    field = '__all__'

admin.site.register(Order,OrderAdmin)