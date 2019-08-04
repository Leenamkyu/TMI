from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RecommendPost
from django.utils import timezone

def main(request):
    posts = RecommendPost.objects
    return render(request, 'Recommend_main.html', {'posts' : posts})

def detail(request, postID):
    post = get_object_or_404(RecommendPost, pk=postID)
    return render(request, 'Recommend_detail.html', {'post' : post})

@login_required
def new(request):
    return render(request, 'Recommend_new.html')

@login_required
def create(request):
    newPost = RecommendPost()
    newPost.title = request.POST['title']
    newPost.body = request.POST['body']
    newPost.update = timezone.datetime.now()

    if request.user.is_authenticated:
        newPost.user = request.user
    else:
        newPost.user = "unknown"

    newPost.save()
    return redirect('recommend_main')

def update(request):
    pass

def delete(request):
    pass