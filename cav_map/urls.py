"""cav_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="cav_map/index.html"), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('map/', TemplateView.as_view(template_name="cav_map/mapDisplay.html"), name='map'),
    path('routemaker/', TemplateView.as_view(template_name="cav_map/coordinateInputs.html"), name='userInput'),
    #path('routemaker/multiPath', TemplateView.as_view(template_name="cav_map/multiPath.html"), name='mapTest'),
    path('routemaker/multiPath', views.create_class, name='mapTest'),
    path('routemaker/savedMP', views.create_class2, name='savedMap'),
    path('forum/', views.forumPostView.as_view(), name='forum'),
    path('createPost/', views.forum_post_create_view, name='createPost')
]
