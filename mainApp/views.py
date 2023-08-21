from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm, AdPostForm
from .models import AdPostModel
from django.utils import timezone


def Homepage(request):
    context = {}
    return render(request, 'home.html', context)


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if user exists
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('loginPage')
        else:
            messages.warning(request, 'Check your details again')
    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('Homepage')


@login_required(login_url='loginPage')
def dashboard(request):
    form = AdPostForm()
    alert = ''
    user_posts = AdPostModel.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AdPostForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            alert = 'alert alert-success'
            messages.success(request, 'Ad Posted Successfully')
        else:
            messages.warning(request, 'Check your details again. Check if you missed enetering any field')
            alert = 'alert alert-danger'

    context = {'form': form, 'alert': alert, 'user_posts': user_posts}
    return render(request, 'dashboard.html', context)


@login_required(login_url='loginPage')
def feed(request):
    posts = AdPostModel.objects.all()
    context = {'posts': posts}
    return render(request, 'feed.html', context)


@login_required(login_url='loginPage')
def AdPostDetailView(request, pk):
    post = get_object_or_404(AdPostModel, id=pk)
    context = {'post': post}
    return render(request, 'AdPostDetail.html', context)


@login_required(login_url='loginPage')
def delete_post(request, pk):
    post = get_object_or_404(AdPostModel, id=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')
    context = {'post': post}
    return render(request, 'deletePost.html', context)


@login_required(login_url='loginPage')
def update_post(request, pk):
    post = get_object_or_404(AdPostModel, id=pk, user=request.user)
    if request.method == 'POST':
        form = AdPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AdPostForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'editPost.html', context)

