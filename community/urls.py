from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename='post')
router.register(r'communitiy', views.CommunityViewSet, basename='communities')

urlpatterns = [
    path("discover/", views.communitiesList, name='discover'),
    path('<int:community_id>/', views.community, name='community'),
    path("new-community/", views.createCommunity, name="new-community"),
    path("api/v1/", include(router.urls)),  # URL's for the post's api
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

