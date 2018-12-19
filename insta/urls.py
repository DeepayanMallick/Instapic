from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('sign-up', views.signup, name='signup'),
    path('ajax-sign-up', views.ajaxsignup),   
    path('ajax-login', views.ajaxlogin),     
    path('logout', views.logout),
    path('upload', views.upload, name='upload'),
    path('ajax-save-photo', views.ajaxsavephoto),
    path('ajax-set-profile-pic', views.ajaxsetprofilepic),
    re_path(r'^(?P<username>[a-zA-Z0-9_]+)$', views.profile),    
    path('ajax-profile-feed', views.ajaxprofilefeed),
    path('ajax-like-photo', views.ajaxlikephoto),
    path('ajax-follow', views.ajaxfollow),
    path('ajax-tag', views.ajaxtag),
    path('ajax-photo-feed', views.ajaxphotofeed)    
]