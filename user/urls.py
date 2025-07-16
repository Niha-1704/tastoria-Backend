from django.urls import path
from .views import login , register
# from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('login/',login),
    path('register/',register)
]