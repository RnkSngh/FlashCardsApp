"""FlashCardProject URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from Users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('app/', include('FlashCardsApp.urls'), name="app"),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
