from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, Context
from blog.models import *
from django.contrib.auth.models import User

def all_users(request):
    users = User.objects.all()
    t = loader.get_template("main.html")
    c = Context({'posts':users})
    return HttpResponse(t.render(c))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/posts")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })