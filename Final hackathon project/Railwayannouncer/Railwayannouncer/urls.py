"""
URL configuration for Railwayannouncer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name = 'main' ),
    path('searchbareng',views.searchbareng, name= 'searchbareng'),
    path('searchbarhindi',views.searchbarhindi, name= 'searchbarhindi'),
    path('searchbarmarathi',views.searchbarmarathi, name= 'searchbarmarathi'),
    path('anounceineng',views.anounceineng, name = 'anounceineng' ),
    path('anounceinhindi',views.anounceinhindi, name = 'anounceinhindi' ),
    path('anounceinmarathi',views.anounceinmarathi, name = 'anounceinmarathi' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)