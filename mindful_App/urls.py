from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Home page
    path('about/', views.about, name='about'),          # About page
    path('articles/', views.articles, name='articles'), # Articles page
    path('booking/', views.booking, name='booking'),    # Booking page
    path('community/', views.community, name='community'), # Community page
    path('moodtracker/', views.moodtracker, name='moodtracker'), # Mood Tracker page
    path('register/', views.register, name='register'), # Register page
    path('resources/', views.resources, name='resources'), # Resources page
    path('tools/', views.tools, name='tools'),          # Tools page
    path('videos/', views.videos, name='videos'),       # Videos page
    path('podcasts/', views.podcasts, name='podcasts'), 
    path('therapists/', views.therapists, name='therapists'), 
    path('faq/', views.faq, name='faq'), 
    path('contact/', views.faq, name='contact'), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.user_login, name='home'), 
    path('appointments/', views.appointment_list, name='appointment_list'),
]

