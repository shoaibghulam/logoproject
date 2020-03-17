from django.contrib import admin
from .models import category,product,logo

class ProductAdmin(admin.ModelAdmin):
    
    list_display=('companyname','logoname','category','price')


class LogoAdmin(admin.ModelAdmin):
    
    list_display=('logoname','category')
# Register your models here.

admin.site.register(category)
admin.site.register(product,ProductAdmin)
admin.site.register(logo,LogoAdmin)