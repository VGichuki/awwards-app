from django.conf.urls import url
from .import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('register/', views.registerPage, name = 'register'),
    url('login/', views.loginPage, name = 'login'),
    # url('logout/', views.logoutUser, name = 'logout'),
]