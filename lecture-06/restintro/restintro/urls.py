"""
URL configuration for restintro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from .views import users, get_or_update_or_delete_user
# from .better_views import UserListCreateAPIView,UserRetrieveUpdateDestroyAPIView
from .custom_api_views import UserListCreateAPIView

urlpatterns = [
    # path('users/', users),
    # path('users/<id>', get_or_update_or_delete_user),
    path('users/', UserListCreateAPIView.as_view(), name='users'),
    # path('users/<id>',UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('admin/', admin.site.urls),
]
