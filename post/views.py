from django.shortcuts import render, HttpResponseRedirect, reverse

from post.models import Post

from post.forms import AddPostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by("-time_created")
    return render(request, "index.html", {"posts": posts})

def newpost(request):
    if request.method == "POST":
        post = AddPostForm(request.POST)
        if post.is_valid():
            data = post.cleaned_data
            Post.objects.create(
                description = data.get("description"),
                roast_or_boast = data.get("r_bool"),
            )
            return HttpResponseRedirect(reverse("homepage"))
    post = AddPostForm()
    return render(request, "newpost.html", {"post": post})


def upvote(request, id):
    post_id = Post.objects.get(id=id)
    post_id.up_vote += 1
    post_id.save()
    return HttpResponseRedirect(reverse("homepage"))

def downvote(request, id):
    post_id = Post.objects.get(id=id)
    post_id.down_vote -= 1
    post_id.save()
    return HttpResponseRedirect(reverse("homepage"))
    
def boasts(request):
    posts = Post.objects.filter(roast_or_boast=False).order_by("-time_created")
    return render(request, "boasts.html", {"posts": posts})
    
def roasts(request):
    posts = Post.objects.filter(roast_or_boast=True).order_by("-time_created")
    return render(request, "roasts.html", {"posts": posts})

def votefilter(request):
    posts = Post.objects.all()
    sorted_posts = sorted(posts, key=lambda x: x.votetotal, reverse=True)
    return render(request, "votefilter.html", {"posts": sorted_posts})