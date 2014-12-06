from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from Projekt3.forms import MyRegistrationForm


@csrf_protect
def loginn(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login/login.html", c)


@csrf_protect
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('login/loggedin.html', RequestContext(request))
    else:
        return HttpResponseRedirect('/posts/invalid')

def all_users(request):
    users = User.objects.all()
    if request.user.is_authenticated():
        user = User.objects.get_by_natural_key(request.user.get_username())
        t = loader.get_template("main.html")
        c = Context({'posts': users, 'user': user})
    else:
        t = loader.get_template("main1.html")
        c = Context({'posts': users})
    return HttpResponse(t.render(c))


def loggedin(request):
    return render_to_response('login/loggedin.html',
                                 {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('login/invalid_login.html')

def logout_view(request):
    logout(request)
    t = loader.get_template("login/logout.html")
    c = Context()
    return HttpResponse(t.render(c))

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/registration_success')
    args ={}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print(args)
    return render_to_response('registration/register.html', args)

def register_success(request):
    return render_to_response('registration/registration_success.html')

def profile(request):
    if request.user.is_authenticated():
        user = User.objects.get_by_natural_key(request.user.get_username())
        t = loader.get_template("profile.html")
        c = Context({'user2': user} )
        return HttpResponse(t.render(c))
    else:
        raise Http404

#errors---
def handler404(request):
    return render(request, 'errors/404.html')

def handler500(request):
    return render(request, 'errors/500.html')

def handler403(request):
    return render(request, 'errors/403.html')

def handler400(request):
    return render(request, 'errors/400.html')

def handler401(request):
    return render(request, 'errors/401.html')
#-----