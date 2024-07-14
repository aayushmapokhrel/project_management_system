from django.urls import path
from user.api.views import register
urlpatterns = [
    path('register',register,name="register")
]
