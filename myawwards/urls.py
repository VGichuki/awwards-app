from django.urls import path
from django.conf.urls import url
from .import views


urlpatterns=[
    path('',views.home,name = 'home'),
    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    url('profile/', views.user_profile, name='profile'),
    url('profile/<username>/', views.update_user_profile, name='userprofile'),
    url('profile/<username>/edit/', views.edit_user_profile, name='editprofile'),
    path('post/', views.post_project, name='new_post'),
    # url(r'^search/', views.search, name='search')
]