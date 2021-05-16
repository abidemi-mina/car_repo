from django.urls import path
from Cars import views

app_name = 'Cars'

urlpatterns = [
   path('about/', views.about, name='about'),
   path('blog-detail/', views.blog_detail, name='blog_detail'),
   path('blog/', views.blog, name='blog'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('register/', views.register, name='register'),
   path('car-detail/', views.car_detail, name='car_detail'),
   path('cars/', views.cars, name='cars'),
   path('contact/', views.contact, name='contact'),
   path('faq/', views.faq, name='faq'),
   path('terms/', views.terms, name='terms'),
   path('team/', views.team, name='team'),
   path('testimonial/', views.testimonial, name='testimonial'),
   path('team-details/<int:team_id>', views.team_details, name='team_details'),
]
