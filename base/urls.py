from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'), 
    path('leaderboard', views.leaderboard_view, name = 'leaderboard') ,
    path('dashboard', views.dashboard_view, name = 'dashboard') ,
    path('message/<int:id>', views.message_view, name = 'message') ,
    path('about', views.about_view, name = 'about') ,
    path('contact', views.contact_view, name = 'contact') ,
    path('blogs', views.blogs_view, name = 'blogs') ,
    path('downloads', views.downloads_view, name = 'downloads') ,
    path('terms_and_conditions', views.terms_conditions_view, name = 'terms_conditions') ,
    path('blog/<str:blog_id>', views.blog_view, name = 'blog') ,
    path('search/users', views.search_user_view, name = 'search_users') 

]