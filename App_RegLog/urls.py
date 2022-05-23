
from django.urls import path
from . import views



app_name = 'RegLog'

urlpatterns = [
    path('singup/', views.sign_up, name='singup'),
    path('login/',views.login_page, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('change_profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='change_pass'),
    path('add_pro_pic/', views.pro_pic, name='add_pro_pic'),
    path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic'),

]
#  RegLog:change_pro_pic
