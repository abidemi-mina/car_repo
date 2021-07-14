from django.urls import path,include
from backend import views
app_name ='backend'

urlpatterns = [

    # path('', views.home, name='home'),
    path('admin-page/', views.index, name='index'),
    path('logout-page/', views.logout, name='logout'),
    path('admin', views.admin, name='admin'),
    path('rent/', views.rent, name='rent'),
    path('foreign/', views.foreign, name='foreign'),
    path('sale/', views.sale, name='sale'),
    path('new/', views.new, name='new'),
    path('addlistings', views.addlistings, name='addlistings'),
    path('edit-list/<int:prop_id>/', views.edit_list, name='edit-list'),
    path('addlocation', views.addlocation, name='addlocation'),
    path('addcars', views.addcar, name='addcar'),
    path('activate', views.activate, name='activate'),
    path('activation_sent', views.activation_sent_view, name='activation_sent'),
    path('view-cars', views.viewcars, name='view-cars'),
    path('change_password', views.change_password, name='change_password'),
    path('createlist', views.createlist, name='createlist'),
    path('editlist', views.editlist, name='editlist'),
    path('userprofile/<int:prop_id>/', views.userprofile, name='userprofile'),
    path('userprofile/<int:prop_id>/', views.updateprofile, name='updateprofile'),
    path('createprofile/<int:prop_id>/', views.createprofile, name='createprofile'),
    path('viewlist', views.viewlist, name='viewlist'),
    path('viewlocation', views.viewlocation, name='viewlocation'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('approve/<int:approve>/', views.approve_car, name='approve'),
    # path('diapprove/<int:disapprove>/', views.disapprove_property, name='disapprove'),
    path('delete/<int:prop_id>/', views.delete, name='delete'),
    path('delet/<int:car>/', views.delete_cartype, name='delcar'),
]
