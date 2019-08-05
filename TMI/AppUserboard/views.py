from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm, CommentForm, SearchForm

def main(request):
    boards = Board.objects
    return render(request, 'Userboard_main.html', {'boards':boards})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id)
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            post = comment_form.save(commit=False)
            post.board_id = board_id
            post.save()
            return redirect('/userboard/detail/' + str(board_id))
    else:
        comment_form=CommentForm()
        context = {
            'board_detail' : board_detail,
            'comments' : comments,
            'comment_form' : comment_form
        }
        return render(request, 'Userboard_detail.html', context)

def new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/userboard/detail/' + str(post.id))
    else:
        form = BoardForm()
        return render(request, 'Userboard_new.html', {'form':form})


def update(request, board_id):
    board=get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.author = form.cleaned_data['author']
            board.text = form.cleaned_data['text']
            board.image = form.cleaned_data['image']
            board.save()
            return redirect('/userboard/detail/' + str(board_id))
    else:
        form = BoardForm(instance=board)
        return render(request, 'Userboard_update.html', {'form':form})  

def delete(request, board_id):
    if request.method == 'POST':
        board = Board.objects.get(pk=board_id)
        board.delete()
        return render(request, 'Userboard_delete.html')
    elif request.method == 'GET':
        return HttpResponse('잘못된 접근입니다.')

def searchtitle(request):
    qs = Board.objects.all()
    q = request.GET.get('q', '')
    if q:
        result = qs.filter(title__icontains=q)
        return render(request, 'Userboard_main.html', {'boards':result, 'q':q})
    else:
        return redirect('userboard_main')

def searchtext(request):
    qs = Board.objects.all()
    q = request.GET.get('q', '')
    if q:
        result = qs.filter(text_icontains=q)
        return render(request, 'Userboard_main.html', {'boards':result, 'q':q})
    else:
        return redirect('userboard_main')