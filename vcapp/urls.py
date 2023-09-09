from django.urls import path
from . import views
urlpatterns = [
    
    
    path('',views.signin,name ='signin'),
    path('signup/',views.signup,name ='signup'),
     path('signout/',views.signup,name ='signout'),
    path('home/',views.home,name ='home'),
    path('newmeeting/',views.newmeeting,name ='newmeeting'),
    path('joinmeeting/',views.joinmeeting,name ='joinmeeting'),

]