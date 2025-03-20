from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename='post')
router.register(r'communitiy', views.CommunityViewSet, basename='communities')

urlpatterns = [
    path("discover/", views.communitiesList, name='discover'),
    path('<int:community_id>/', views.community, name='community'),
    path("api/v1/", include(router.urls)),  # URL's for the post's api
]
