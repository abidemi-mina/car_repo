from django.contrib import admin
from .models import Blog, Comment
from Cars.models import *
admin.site.site_header='Car Dealer Website'


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'content', 'post', 'time', 'active')
#     list_filter = ('active', 'time')
#     search_fields = ('name', 'email', 'content')
#     actions = ['approve_comments']

    
#     def approve_comments(self, request, queryset,):
#         queryset.update(active = True)

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
admin.site.register(Comment)





