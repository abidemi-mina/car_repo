"""cars_env URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Cars import views
from django.contrib.auth import views as auth_views #import this
from django.conf import settings
from django.conf.urls.static import static
from backend.views import activation_sent_view, activate




urlpatterns = [
    path('', views.home, name='home'),
    path('pages/', include('Cars.urls')),
    path('backend/', include('backend.urls')),
    path('whobe-20-42/', admin.site.urls),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='htmls/password-rest-done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="htmls/password-reset-confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='htmls/password-reset-complete.html'), name='password_reset_complete'),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

