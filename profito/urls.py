"""profito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from .views import home
from Users.views import signup
from django.contrib.auth import views as auth_views
from Feeds.views import (ads, ad_detail)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls), 
    path('signup/', signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'profito/home.html'}, 
        name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('ads/', ads, name="ads"),
    path('ad_detail/(?P<id>\d+)/', ad_detail, name="ad_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
