from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.urls import reverse_lazy
from AppCompanion.models import Companion


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('signupdone')

class RegisteredView(TemplateView):
    template_name = 'registration/signupdone.html'


def Viewposts(request):
    qs = Companion.objects.all()
    q = request.user.username
    result = qs.filter(user__icontains=q)
    return render(request, 'profile.html', {'boards':result, 'q':q})