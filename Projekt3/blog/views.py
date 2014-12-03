from django.http import HttpResponse
from django.template import loader, Context
from blog.models import *
from django.contrib.auth.models import User

def all_users(request):
    users = User.objects.all();
    t = loader.get_template("main.html")
    c = Context({'posts':users})
    return HttpResponse(t.render(c))