from django.urls import path

from . import views
# from views import profile_user

app_name='accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.Register, name="register"),
    path('login', views.Login, name="login"),
    path('profile', views.profile_user, name="profile"),
    path('logout', views.Logout, name="logout"),
]
