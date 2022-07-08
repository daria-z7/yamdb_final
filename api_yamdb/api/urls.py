from api.views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, get_jwt_token,
                       register)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

api_v1_router = DefaultRouter()
api_v1_router.register('users', UserViewSet)
api_v1_router.register('titles', TitleViewSet, basename='titles')
api_v1_router.register('genres', GenresViewSet, basename='genres')
api_v1_router.register('categories', CategoriesViewSet, basename='categories')
api_v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
api_v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(api_v1_router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
]
