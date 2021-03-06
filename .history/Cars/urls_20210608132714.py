from django.urls import path
from Cars import views

app_name = 'Cars'

urlpatterns = [
   path('about/', views.about, name='about'),
   path('blog-detail/<int:pk>/', views.blog_detail, name='blog_detail'),
   path('blog/', views.blog, name='blog'),
   path('login-view/', views.login_view, name='login_view'),
   path('dashboard/', views.dashboard, name='dashboard'),

   path('logout/', views.logout, name='logout'),
   path('register/', views.register, name='register'),
   path('car-detail/<int:car_id>/', views.car_detail, name='car_detail'),
   path('cars/', views.cars, name='cars'),
   path('contacts-page/', views.contacts, name='contacts'),
   path('team/', views.team, name='team'),
   path('team-details/<int:team_id>', views.team_details, name='team_details'),
   
]
