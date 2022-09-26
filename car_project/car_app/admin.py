from django.contrib import admin

# Register your models here.
from .models import Cars,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ['name','slug','desc',]
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Cars,CarAdmin)
