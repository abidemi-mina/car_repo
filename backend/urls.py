from django.urls import path,include
from backend import views
app_name ='backend'

urlpatterns = [

    # path('', views.home, name='home'),
    path('admin-page/', views.index, name='index'),
    path('logout-page/', views.logout, name='logout'),
    path('admin', views.admin, name='admin'),
    path('addlistings', views.addlistings, name='addlistings'),
    path('addlocation', views.addlocation, name='addlocation'),
    path('addcars', views.addcar, name='addcar'),
    path('view-cars', views.viewcars, name='view-cars'),
    path('change_password', views.change_password, name='change_password'),
    path('createlist', views.createlist, name='createlist'),
    path('editlist', views.editlist, name='editlist'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('viewlist', views.viewlist, name='viewlist'),
    path('viewlocation', views.viewlocation, name='viewlocation'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('approve/<int:approve>/', views.approve_property, name='approve'),
    path('diapprove/<int:disapprove>/', views.disapprove_property, name='disapprove'),
    path('delete/<int:prop_id>/', views.delete_property, name='delete'),
    path('delete/<int:car>/', views.delete_cartype, name='delcar'),
]
