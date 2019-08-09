from django.shortcuts import render, redirect,get_object_or_404
from .models import Companion
from django.core.paginator import Paginator
from .forms import CompanionPost
from django.utils import timezone
from django.contrib.auth.decorators import login_required 
import datetime #문자열을 Date type으로 바꿀때 사용 

# Create your views here.
def main(request):
    companions = Companion.objects
    companion_list = Companion.objects.all()
    paginator = Paginator(companion_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'Companion_main.html', {'companions': companions, 'posts':posts})

#새 글쓰기 기능 
@login_required
def new(request):
    if request.method == 'POST':
        form = CompanionPost(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
                    
            if request.user.is_authenticated:
                post.user = request.user
            else: 
                post.user = "unknown"    
            
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
    q_category = request.GET.get('category','')

    #새로추가 8/9######
    q_start_date = request.GET.get('start_date','')
    q_end_date = request.GET.get('end_date','')
    ###########

    #사용자가 입력한 값이 있는지 확인 후 순차적으로 필터링을 거침
    if q_category:
        qs = qs.filter(category = q_category)
    if q_country:
        qs = qs.filter(country = q_country)
    if q_city:
        qs = qs.filter(city = q_city)
    if q_bucket_list:
        qs = qs.filter(bucket_list = q_bucket_list)
    if q_body:
        qs = qs.filter(body = q_body)

    ######새로추가 8/9########## => 미완성: 시작날짜보다 같거나 크면 filter, 마지막일보다 작거나 같으면 filter 하도록 수정하기(일부 수정완료 - 조건 다시 확인하기)    
    if q_start_date:
        q_start_date = datetime.datetime.strptime(q_start_date, '%m/%d/%Y') # '/'로 나뉘어진 문자열 형태의 날짜를 dateField type으로 변환    
        qs = qs.filter(end_date__gte = q_start_date)

    if q_end_date:
        q_end_date = datetime.datetime.strptime(q_end_date, '%m/%d/%Y')
        qs = qs.filter(end_date__lte = q_end_date)
    ###########        
    
    #필터링 된 객체 리스트와 검색값 반환
    return render(request, 'Companion_search.html', {'result_list': qs, 'search': q_country})

def update(request, pk):
    companion = get_object_or_404(Companion, pk = pk)
    
    if request.method == 'POST':
        form = CompanionPost(request.POST, request.FILES)    
        if form.is_valid():
            companion.status = form.cleaned_data['status'] #cleaned_date : 값들을 사전형 데이터로 반환 ex) {'title': 수정값}
            companion.category = form.cleaned_data['category']
            companion.title = form.cleaned_data['title']
            companion.country = form.cleaned_data['country']
            companion.city = form.cleaned_data['city']
            companion.bucket_list = form.cleaned_data['bucket_list']
            companion.body = form.cleaned_data['body']

            ####새로추가 8/9    
            companion.start_date = form.cleaned_data['start_date']
            companion.end_date = form.cleaned_data['end_date']
            #######

            companion.save()
            return redirect('companion_main')
    else:
        form = CompanionPost(instance = companion)         
        return render(request, 'Companion_update.html', {'form':form})        

def delete(request, pk):
    companion = get_object_or_404(Companion, pk = pk)
    companion.delete()
    return redirect('companion_main')
