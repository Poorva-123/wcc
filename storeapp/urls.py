from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from storeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('link-twitter-account/', views.link_twitter_account, name='link_twitter_account'),
    path('twitter/auth/', views.get_twitter_auth, name='twitter_auth'),
    path('twitter/callback/', views.twitter_callback, name='twitter_callback'),
    path('terms_of_services/', views.terms_of_service, name='terms_of_service'),  # Updated URL pattern
]
