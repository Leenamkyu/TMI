from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm, CommentForm, SearchForm

def main(request):
    boards = Board.objects
    return render(request, 'Userboard_main.html', {'boards':boards})

def warning(request):
    return render(request, 'Userboard_warning.html')

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id)
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            post = comment_form.save(commit=False)
            post.author = request.user.username
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

@login_required
def new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
            if request.user.is_authenticated:
                post.author = request.user.username
            else:
                post.author = "unknown"

            post.save()
            return redirect('/userboard/detail/' + str(post.id))
    else:
        form = BoardForm()
        return render(request, 'Userboard_new.html', {'form':form})


@login_required
def update(request, board_id):
    board=get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.text = form.cleaned_data['text']
            board.image = form.cleaned_data['image']
            if board.author == request.user.username:
                board.save()
                return redirect('/userboard/detail/' + str(board_id))
            else:
                return redirect('/userboard/warning')
    else:
        form = BoardForm(instance=board)
        return render(request, 'Userboard_update.html', {'form':form})  

@login_required
def delete(request, board_id):
    if request.method == 'POST':
        board = Board.objects.get(pk=board_id)
        if board.author == request.user.username:
            board.delete()
            return render(request, 'Userboard_delete.html')
        else:
            return redirect('/userboard/warning')
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