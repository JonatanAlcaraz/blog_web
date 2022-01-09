"""blogCrud URL Configuration

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
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    like,
    login_view,
    logout_view,
    signup_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view, name= 'login'),
    path('logout/',logout_view, name= 'logout'),
    path('signup/',signup_view, name= 'signup'),
    #path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(), name= 'list'),
    path('create/', PostCreateView.as_view(), name= 'create'),
    path('<slug>/', PostDetailView.as_view(), name= 'detail'),
    path('<slug>/update/', PostUpdateView.as_view(), name= 'update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name= 'delete'),
    path('like/<slug>/', like, name= 'like')
    
]

handler404 = 'posts.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_URL )
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_URL )

