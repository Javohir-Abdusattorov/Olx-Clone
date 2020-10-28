
from django.contrib import admin
from .models import ( Category, SubCategory, ProductParent, ProductPhone, ProductCar, ProductHouse, ProductFurniture, ProductWatch, ProductApartment )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'address', 'created_at')
    

class ProductPHONEAdmin(admin.ModelAdmin):
    list_display = ('parent_product', 'price', 'seller')


class ProductCARAdmin(admin.ModelAdmin):
    list_display = ('parent_product', 'price', 'seller')


class ProductHOUSEAdmin(admin.ModelAdmin):
    list_display = ('parent_product', 'price', 'seller')


class ProductFURNITUREAdmin(admin.ModelAdmin):
    list_display = ('parent_product', 'price', 'seller')


class ProductWATCHAdmin(admin.ModelAdmin):
    list_display = ('parent_product', 'price', 'seller')


class ProductAPARTMENTAdmin(admin.ModelAdmin):
    list_display = ('parent_product', 'price', 'seller')
    
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ProductParent, ProductAdmin)
admin.site.register(ProductPhone, ProductPHONEAdmin)
admin.site.register(ProductCar, ProductCARAdmin)
admin.site.register(ProductHouse, ProductHOUSEAdmin)
admin.site.register(ProductFurniture, ProductFURNITUREAdmin)
admin.site.register(ProductWatch, ProductWATCHAdmin)
admin.site.register(ProductApartment, ProductAPARTMENTAdmin)
