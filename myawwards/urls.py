from django.conf.urls import url
from .import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('register/', views.registerPage, name = 'register'),
    url('login/', views.loginPage, name = 'login'),
    url('logout/', views.logoutUser, name = 'logout'),
    url('profile/', views.user_profile, name='profile'),
    url('profile/<username>/', views.update_user_profile, name='userprofile'),
    # url(r'^search/', views.search, name='search')
]