from django.urls import path
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name = 'home'),
    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    url('profile/', views.user_profile, name='profile'),
    url('profile/<username>/', views.update_user_profile, name='userprofile'),
    url('profile/<username>/edit/', views.edit_user_profile, name='editprofile'),
    path('project/', views.project, name='project'),
    # url(r'^search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)