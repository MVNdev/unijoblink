from django.urls import path
from .views import Login, RegisterUser, Logout


urlpatterns = [
    path('', Login, name='login'),
    path('registro/', RegisterUser, name='register'),
    path('logout/', Logout, name='logout'),
]