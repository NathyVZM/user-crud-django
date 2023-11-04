from rest_framework.routers import DefaultRouter
from django.urls import path
from .api.views import UserViewSet

user_router = DefaultRouter()
user_router.register(prefix='user', basename='user', viewset=UserViewSet)

urlpatterns = [
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
] + user_router.get_urls()
