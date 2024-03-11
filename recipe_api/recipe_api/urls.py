# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes import views
from rest_framework.authtoken import views as rviews
from recipes.views import CreateUser
router = DefaultRouter()
router.register('recipe', views.RecipeView)
router.register('review', views.ReviewView)

urlpatterns = [
    path('users/', CreateUser.as_view({'post': 'create'}), name='user-create'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', rviews.obtain_auth_token),
    path('api/', include('recipes.urls')),
]
