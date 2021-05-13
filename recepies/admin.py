from django.contrib import admin
from recepies.models import Recepies, Category

class RecepiesAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recepies, RecepiesAdmin)
admin.site.register(Category, CategoryAdmin)
