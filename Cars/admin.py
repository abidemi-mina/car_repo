from django.contrib import admin
from Cars.models import *
admin.site.site_header='Car Dealer Website'

# Register your models here.
admin.site.register(DealerInfo)
admin.site.register(Blog)
admin.site.register(CarType)
admin.site.register(Cars)
admin.site.register(Team)
admin.site.register(Brands)
admin.site.register(CarEngine)
admin.site.register(ContactDealer)
admin.site.register(Location)

