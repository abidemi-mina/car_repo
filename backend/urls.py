from django.urls import path,include
from backend import views
app_name ='backend'

urlpatterns = [

<<<<<<< HEAD
    # path('', views.home, name='home'),
    path('admin-page/', views.index, name='index'),
    path('logout-page/', views.logout, name='logout'),
=======
    path('', views.index, name='index'),
    path('addlisting', views.addlisting, name='addlisting'),
    path('addlistings', views.addlisting, name='addlistings'),
    path('addlocation', views.addlocation, name='addlocation'),
    path('changepas', views.changepas, name='changepas'),
    path('createlist', views.createlist, name='createlist'),
    path('editlist', views.editlist, name='editlist'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('viewlist', views.viewlist, name='viewlist'),
    path('viewlocation', views.viewlocation, name='viewlocation'),
>>>>>>> 358ac0b8db5e182c5bdb5723441e7d9a260cd9e3
    path('admin-logout/', views.admin_logout, name='admin_logout'),
]
