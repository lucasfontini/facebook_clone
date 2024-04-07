from django.contrib import admin
from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home ,name='home'),
    path('chat/', Chat ,name='chat'),

    path('home/', home ,name='home'),
     path("login/", LoginView.as_view(), name='login'),
     path('login_submit/', LoginSubmit, name='login_submit'),
    path('logout/<int:id>', Logout, name='Logout'),   
    path('myprofile/<int:id>', MyProfile, name='MyProfile'),     
    path('create_post/', Create_post, name='create_post'),  
    path('post/like/<int:id>', LikePost, name='LikePost'),       
    path('post/delete/<int:id>', DeletePost, name='DeletePost'),    
       
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
