from customuser_app.models import MyUser
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from django.conf import settings
from customuser_app.forms import LoginForm, SignUp

# Create your views here.

def index(request):
    new_user = settings.AUTH_USER_MODEL
    # print(dir(request.user))
    return render(request, 'index.html', {'user': new_user})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user: 
                login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, "generic_form.html", {'form' : form})


def loggedOut_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


def signUp_view(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = form.save()
            user.refresh_from_db()
            user.save()
            password = form.cleaned_data.get('password')
            user = authenticate(MyUser.objects.create_user(username=data['username'], password=data['password'], email=data['email'], homepage=data['homepage'], displayname=data['displayname'], age=data['age']))
            login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = SignUp()
    return render(request, "generic_form.html", {'form' : form})
