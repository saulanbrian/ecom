from django.contrib import admin

from .models import Product, Review
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  readonly_fields = ['rating_ave']

class ReviewAdmin(admin.ModelAdmin):
  readonly_fields = ['image']

admin.site.register(Product,ProductAdmin)
admin.site.register(Review,ReviewAdmin)

