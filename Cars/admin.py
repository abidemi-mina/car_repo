from django.contrib import admin
from Cars.models import *
admin.site.site_header='Car Dealer Website'

# Register your models here.
admin.site.register(Dealer_Info)
admin.site.register(Blog)
admin.site.register(Car_Type)
admin.site.register(Cars)
admin.site.register(Team)
admin.site.register(Brands)
admin.site.register(Car_Engine)
admin.site.register(Contact_Dealer)
admin.site.register(Location)

