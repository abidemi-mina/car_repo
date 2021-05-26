from django.urls import path,include
from backend import views
app_name ='backend'

urlpatterns = [

    # path('', views.home, name='home'),
    path('admin-page/', views.index, name='index'),
    path('logout-page/', views.logout, name='logout'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
]
