from django.urls import path
from . import views

urlpatterns = [
    path("discover/", views.showCommunities, name="communities"),
    path("<int:community_id>/", views.community, name="community"),
    path("<int:community_id>/join", views.joinCommunity, name="join_community"),
    path("<int:community_id>/new-post", views.makePost, name="new_post"),
]
