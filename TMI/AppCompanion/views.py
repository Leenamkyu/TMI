from django.shortcuts import render, redirect,get_object_or_404
from .models import Companion
from django.core.paginator import Paginator
from .forms import CompanionPost
from django.utils import timezone
from django.contrib.auth.decorators import login_required # 새로 추가

# Create your views here.
def main(request):
    companions = Companion.objects
    companion_list = Companion.objects.all()
    paginator = Paginator(companion_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'Companion_main.html', {'companions': companions, 'posts':posts})

#새 글쓰기 기능 
# @login_required
def new(request):
    if request.method == 'POST':
        form = CompanionPost(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            
            #####새로 추가 부분 1 ######
            # if request.user.is_authenticated:
            #     post.user = request.user
            # else: 
            #     post.user = "unkown" 
            #########

            post.save()
            return redirect('companion_main')
    else:
        form = CompanionPost()
        return render(request, 'Companion_new.html', {'form':form})        

#검색기능 
def search(request):
    qs = Companion.objects.all()
  
    q_country = request.GET.get('country','')
    q_city    = request.GET.get('city','')
    q_bucket_list = request.GET.get('bucket_list','')
    q_body = request.GET.get('body','')

    #사용자가 입력한 값이 있는지 확인 후 순차적으로 필터링을 거침
    if q_country:
        qs = qs.filter(country = q_country)
    if q_city:
        qs = qs.filter(city = q_city)
    if q_bucket_list:
        qs = qs.filter(bucket_list = q_bucket_list)
    if q_body:
        qs = qs.filter(body = q_body)
    
    #필터링 된 객체 리스트와 검색값 반환
    return render(request, 'Companion_search.html', {'result_list': qs, 'search': q_country})

def update(request, pk):
    companion = get_object_or_404(Companion, pk = pk)
    form = CompanionPost(request.POST, instance = companion)

    if form.is_valid():
            form.save()
            return redirect('companion_main')

    return render(request, 'Companion_new.html', {'form':form})        

def delete(request, pk):
    companion = get_object_or_404(Companion, pk = pk)
    companion.delete()
    return redirect('companion_main')
