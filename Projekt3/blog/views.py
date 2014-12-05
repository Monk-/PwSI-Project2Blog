from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def loginn(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login/login.html",c)


@csrf_protect
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('login/loggedin.html',RequestContext(request))
    else:
        return HttpResponseRedirect('/posts/invalid')

def all_users(request):
    users = User.objects.all()
    t = loader.get_template("main.html")
    c = Context({'posts':users})
    return HttpResponse(t.render(c))


def loggedin(request):
    return render_to_response('login/loggedin.html',
                                 {'full_name' : request.user.username})

def invalid_login(request):
    return render_to_response('login/invalid_login.html')

def logout(request):
    logout(request)
    return render_to_response('login/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/registration_success')
    args ={}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    print(args)
    return render_to_response('registration/register.html',args)

def register_success(request):
    return render_to_response('registration/registration_success.html')


