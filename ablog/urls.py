from django.contrib import admin
from django.urls import path
from app1.models import *
from app1.views import HomeView, Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
