from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    # path('signup', views.signup, name='home'),
    path('home', views.home, name='home'),
]