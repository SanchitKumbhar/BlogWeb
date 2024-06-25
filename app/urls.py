"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from app import views
urlpatterns = [
    path("",views.index,name=""),
    # path("authenticate",views.authenticate,name="authenticate"),
    path("signup",views.signuppage,name="signup"),
    path("login",views.loginuserpage,name="login"),
    path("login-user",views.loginuser,name="login-user"),
    path("signup-user",views.signup_user,name="signup-user"),
    path("personal-details",views.personal_details,name="personal-details"),
    path("Dashboard",views.Dashboard,name="Dashboard"),
    path("personal-details-registered",views.personal_details_registered,name="personal-details-registered"),
    path("blog-content-save",views.blog_content_save,name="blog-content-save"),
    path("blog/<int:idip>",views.ip_view,name="blog"),
    path("like/<int:pkid>",views.like_view,name="like"),
    # path("dislike/<int:pkid>",views.dislike_view,name="dislike"),
    path("blog/comment/<int:blogid>",views.comment_view,name="comment"),
    path("blog/<int:blogid>",views.comment_view,name="comment"),
]
