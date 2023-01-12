from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.Loginuser,name="login"),
    path('register/',views.RegisterUser,name="register"),
    path('logout/',views.Logoutuser,name="logout"),
    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>/',views.userProfile,name='user_profile'),
    path('account/',views.userAccount,name='account'),
    path('edit_account/',views.editaccount,name='edit_account'),
    path('inbox/',views.inbox,name='inbox'),
    path('message/<str:pk>/',views.viewMessage,name='message'),
    path('send_message/<str:pk>/',views.createMessage,name="create_message")
]
