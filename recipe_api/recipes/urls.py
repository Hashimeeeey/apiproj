from django.urls import path
from .views import CreateUser, RecipeView, ReviewView

app_name = 'recipes'
urlpatterns = [
    path('users/', CreateUser.as_view({'post': 'create'}), name='user-create'),
    path('recipes/', RecipeView.as_view({'get': 'list', 'post': 'create'}), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='recipe-detail'),
    path('reviews/', ReviewView.as_view({'get': 'list', 'post': 'create'}), name='review-list-create'),
]