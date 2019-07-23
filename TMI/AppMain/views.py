from django.shortcuts import render

# AppMain views

def home(request):
    return render(request, 'home.html')

