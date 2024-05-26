from django.contrib import admin
from djangoProject.models import User,Product

# admin.site.register(User)
# admin.site.register(Product)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['title','name','username','email']
    list_display = ['title','name','username']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['seller','name','price','description','stock']
    search_fields = ['name']
    list_display = ['id','name','price']
    save_as = True

