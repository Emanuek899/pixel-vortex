"""
This module controls all the options over the community section
such show communities, join communities etc...
"""
from . import models
from rest_framework import viewsets, filters
from . import serializers
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allow posts to be viewed or edited
    """
    queryset = models.Post.objects.all().order_by("-created_at")
    serializer_class = serializers.PostSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class CommunityViewSet(viewsets.ModelViewSet):
    """
    Api endpoint for communities
    """
    queryset = models.Community.objects.all().order_by('-creation_date')
    serializer_class = serializers.CommunitySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['community_name']

    def get_queryset(self):
        """
        This function allows to get all the coincidences with
        the search term and return a queryset
        """
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', None)

        if search_term:
            queryset = queryset.filter(community_name__icontains=search_term)
            # Aquí se realiza la búsqueda case-insensitive
        return queryset


def communitiesList(request):
    """
    Show all the communities
    """
    return render(request, 'community/communities.html')


def community(request, community_id):
    """
    Show a specific community
    """
    context = {
        'community_id': community_id
    }
    return render(request, 'community/community.html', context)
