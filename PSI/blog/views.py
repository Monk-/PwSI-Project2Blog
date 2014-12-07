from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader, Context, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect
from PSI.forms import *
from blog.models import *
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    users = User.objects.all()
    if request.user.is_authenticated():
        user = User.objects.get_by_natural_key(request.user.get_username())
        t = loader.get_template("main.html")
        c = Context({'users': users,
                     'user': user,
                     'categories': Category.objects.all(),
                     'posts': Post.objects.all()})
    else:
        t = loader.get_template("main1.html")
        c = Context({'users': users,
                     'categories': Category.objects.all(),
                     'posts': Post.objects.all()})
    return HttpResponse(t.render(c))


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated():
        user = User.objects.get_by_natural_key(request.user.get_username())
        t = loader.get_template("view_post.html")
        c = Context({'user': user,
                    'post': post})
    else:
        t = loader.get_template("view_post_log_out.html")
        c = Context({'post': post})
    return HttpResponse(t.render(c))


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.user.is_authenticated():
        user = User.objects.get_by_natural_key(request.user.get_username())
        t = loader.get_template("view_category.html")
        c = Context({'user': user,
                     'category': category,
                     'posts': Post.objects.filter(categories=category)})
    else:
        t = loader.get_template("view_category_log_out.html")
        c = Context({'category': category,
                     'posts': Post.objects.filter(categories=category)})
    return HttpResponse(t.render(c))



###########LOGINS
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
            return render_to_response('login/loggedin.html',RequestContext(request))
    else:
        return HttpResponseRedirect('/posts/invalid')


def loggedin(request):
       user = User.objects.get_by_natural_key(request.user.get_username())
       t = loader.get_template("login/loggedin.html")
       c = Context({'full_name' : request.user.username ,'user':user})
       return HttpResponse(t.render(c))




def invalid_login(request):
    return render_to_response('login/invalid_login.html')


def logout_view(request):
    logout(request)
    return render_to_response('login/loginout.html')


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile1 = profile_form.save(commit=False)
            profile1.user = user
            if 'picture' in request.FILES:
                profile1.picture = request.FILES['picture']
            profile1.save()
            return HttpResponseRedirect('/posts/registration_success')
    args = {}
    args.update(csrf(request))
    args['user_form'] = UserForm()
    args['profile_form'] = UserProfileForm()
    print(args)
    return render_to_response('registration/register.html', args)


def register_success(request):
    return render_to_response('registration/registration_success.html')


def profile(request):
    if request.user.is_authenticated():
        user = User.objects.get_by_natural_key(request.user.get_username())
        u = User.objects.get(username= request.user.get_username())
        s = u.oser.picture
        t = loader.get_template("profile.html")
        c = Context({'user2': user, 'image': s})
        return HttpResponse(t.render(c))
    else:
        raise Http404

#ERRORS---
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