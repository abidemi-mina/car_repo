from django.urls import path
from Cars import views


app_name = 'Cars'

urlpatterns = [
   path('home-page/' , views.home2 , name='home2'),
   path('home-page2/' , views.home3 , name='home3'),
   path('about/', views.about, name='about'),
   path('blog-detail/<int:pk>/', views.blog_detail, name='blog_detail'),
   path('blog-detail2/<int:blog_id>/', views.blog_detail2, name='blog_detail2'),
   path('blog-detail3/<int:blog_id>/', views.blog_detail3, name='blog_detail3'),
   path('search/', views.search, name='search'),
   path('blog/', views.blog, name='blog'),
   path('blog2/', views.blog2, name='blog2'),
   path('blog3/', views.blog3, name='blog3'),
   path('login-view/', views.login_view, name='login_view'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('addlistings', views.addlistings, name='addlistings'),
   path('addlistings2', views.addlistings2, name='addlistings2'),
   path('logout/', views.logout, name='logout'),
   path('register/', views.register, name='register'),
   path('filter/', views.filter_form, name='form'),
   path('car-detail/<int:car_id>/', views.car_detail, name='car_detail'),
   path('car-detail2/<int:car_id>/', views.car_detail2, name='car_detail2'),
   path('car-detail3/<int:car_id>/', views.car_detail3, name='car_detail3'),
   path('contact/', views.contact, name='contact'),
   path('motors/', views.cars, name='motor'),
   path('motors2/', views.cars2, name='motor2'),
   path('motors3/', views.cars3, name='motor3'),
   path('team/', views.team, name='team'),
   path('team2/', views.team2, name='team2'),
   path('team3/', views.team3, name='team3'),
   path('team-details3/<int:team_id>', views.team_details3, name='team_details3'),
   path('team-details/<int:team_id>', views.team_details, name='team_details'),
   path('team-details2/<int:team_id>', views.team_details2, name='team_details2'),
   path("password_reset", views.password_reset_request, name="password_reset")
      
]

