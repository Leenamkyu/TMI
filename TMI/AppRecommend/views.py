from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import RecommendPost, Comment
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewPost
import json


def main(request):
    posts = RecommendPost.objects
    return render(request, 'Recommend_main.html', {'posts' : posts})


def detail(request, postID):
    post = get_object_or_404(RecommendPost, pk=postID)
    return render(request, 'Recommend_detail.html', {'post' : post})


@login_required
def create(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid:
            newPost = form.save(commit=False)
            newPost.update = timezone.now()
            if request.user.is_authenticated:
                newPost.user = request.user
            else:
                newPost.user = "unknown"
            newPost.save()
            return redirect('recommend_main')
    else:
        form = NewPost()
        return render(request, 'Recommend_new.html', {'form' : form})


@login_required
def update(request, postID):
    post = get_object_or_404(RecommendPost, pk=postID)
    form = NewPost(request.POST, instance=post)

    if form.is_valid():
        form.save()
        return redirect('recommend_main')
    
    return render(request, 'Recommend_new.html', {'form' : form})


@login_required
def delete(request, postID):
    post = get_object_or_404(RecommendPost, pk=postID)
    post.delete()
    return redirect('recommend_main')


@login_required
@require_POST
def like(request):
    user = request.user
    post = get_object_or_404(RecommendPost, pk = request.POST['postID'])

    if post.likes.filter(id = user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    ret = {
        'num' : post.like_count(),
    }

    return HttpResponse(json.dumps(ret), content_type="application/json")


@login_required
@require_POST
def create_comment(request):
    comment = Comment()
    comment.author = request.user
    comment.text = request.POST['body']
    comment.post = get_object_or_404(RecommendPost, pk = request.POST['postID'])
    comment.save()

    ret = {
        'text' : comment.text,
        'time' : comment.created_date,
        'author' : comment.author,
    }

    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder, default=json_converter), content_type="application/json")


def json_converter(obj):
    if isinstance(obj, User):
        return obj.__str__()


@login_required
def remove_comment(request, postID, cpk):
    post = get_object_or_404(RecommendPost, pk = postID)
    comment = Comment.objects.get(pk=cpk)
    if not comment.author == request.user:
        return redirect('recommend_detail', postID)
    else:
        comment.delete()
        return redirect('recommend_detail', postID)