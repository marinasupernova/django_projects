from django.contrib import admin
from addntravel.models import Travel

class TravelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Travel, TravelAdmin)

