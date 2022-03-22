"""delivery URL Configuration

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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from comments.views import CommentViewSet
from parties.views import PartyViewSet, ParticipantViewSet
from users.views import UserViewSet

root_router = DefaultRouter()
root_router.register('parties', PartyViewSet)
root_router.register('users', UserViewSet)

comments_router = NestedDefaultRouter(root_router, 'parties', lookup='party')
comments_router.register('comments', CommentViewSet)

participants_router = NestedDefaultRouter(root_router, 'parties', lookup='party')
participants_router.register('participants', ParticipantViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(root_router.urls)),
    path('api/v1/', include(comments_router.urls)),
    path('api/v1/', include(participants_router.urls)),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/', include('allauth.urls')),
    # Swagger:
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
