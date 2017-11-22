from django.shortcuts import render, redirect
from django.contrib import messages
from . models import UserManager, Users, List, Contribute

# Create your views here.
def index(request):
    context = {
        "Users": Users.objects.all(),
    }
    return render(request, "main/index.html", context)

def register(request):
    errors = Users.objects.validator(request.POST)
    if 'err_messages' in errors:
        for error in errors['err_messages']:
            messages.error(request, error)
        return redirect('/')
    else: 
        return redirect('/quotes')

def login (request):
    print session
    return render(request, '/quotes')

def quotes(request):
    context = {
        "Users": Users.objects.all(),
    }
    return render(request, 'main/quotes.html', context)

def main(request):
    context = {
        "Users": Users.objects.all(),
    }
    return render(request, 'main/quotes.html', context)
 
def update(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main/index' + id)
    else: 
        users = Users.objects.get(id = id)
        users.name = request.POST['name']
        users.desc = request.POST['desc']
        users.save()
        return redirect('/quotes')

def dashboard(request):
    return redirect('/quotes')

def contribute(request):
    print request.POST    
    return render(request, '/quotes')

def users(request):
    print request.POST
    return render(request, 'main/users.html')

def logout(request):
    return redirect('/')