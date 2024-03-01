from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
  readonly_fields = ('product','amount','date_placed','date_received','received','buyer')

admin.site.register(Order,OrderAdmin)