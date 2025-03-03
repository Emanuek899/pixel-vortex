from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def showCommunities(request):
    # Get all the communities and give it to the page as context
    community = models.Community.objects.all()
    return render(request, "community/community.html", {"communities": community})

@login_required
def community(request, community_id):
    # Check if a community exist (is and instance of Community) by id
    community = get_object_or_404(models.Community, community_id=community_id)
    return render(request,"community/community_detail.html", {"community": community})


@login_required
def joinCommunity(request, community_id):
    # Get the comuunity bi his id
    community= get_object_or_404(models.Community, community_id=community_id)

    # Checks if the user is not in the community, if not in, then he can join
    if request.user not in community.users.all():
        community.users.add(request.user)
        community.users_count = community.users.count()
        community.save()
    
    return redirect("community", community_id=community_id)