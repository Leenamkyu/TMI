from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'Userboard_main.html')

def detail(request):
    pass

@login_required
def new(request):
    return render(request, 'Userboard_new.html')

@login_required
def create(request):
    pass

def update(request):
    pass

def delete(request):
    pass