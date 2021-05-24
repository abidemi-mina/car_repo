from django.urls import path,include
from backend import views
app_name ='backend'

urlpatterns = [

    path('', views.index, name='index'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
]
