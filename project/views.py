from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Task, UserProfile
from .forms import TaskForm, CustomUserCreationForm, ProfileCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    user = request.user
    form = TaskForm()
    tasks = Task.objects.filter(user=user)
    template = 'project/index.html'
    empty = True if len(tasks) == 0 else False

    if request.method == 'POST':
        form = TaskForm(request.POST)

        curr_task = Task(user=request.user, name=request.POST['name'])
        curr_task.save()
            
        return redirect("/")
    return render(request, template, {'tasks': tasks, 'form': form, 'empty': empty, 'user':user})

@login_required(login_url='login')
def editTask(request, pk):
    tasks = Task.objects.filter(user=request.user)
    curr_task = Task.objects.get(id=pk)
    form = TaskForm(instance=curr_task)
    template = 'project/index.html'

    if request.method == "POST":
        form = TaskForm(request.POST, instance=curr_task)
        curr_task.name = request.POST['name']
        curr_task.save()
        return redirect('home')

    return render(request, template, {'form':form, 'tasks':tasks})

@login_required(login_url='login')
def deleteTask(request, pk = None):
    task = get_object_or_404(Task, pk=pk)
    task.instance = task
    task.delete()
    return redirect('home')


@login_required(login_url="login")
def viewProfile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    page = 'viewprofile' 
    return render(request, "project/profiles.html", {'profile': profile, 'page': page, 'user':user})


def loginPage(request):
    page = 'login'

    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'project/login.html', {
        'page': page
    })


def logoutPage(request):
    logout(request)
    return redirect('login')

    
def signupPage(request):
    page = 'signup'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('addprofile')

    return render(request, 'project/login.html', {
        'page': page, 
        'form': form,
    })


@login_required(login_url='login')
def addProfile(request):
    user = request.user
    form = ProfileCreationForm()

    if request.method == "POST":
        
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            if 'dark_mode' in request.POST:
                UserProfile.objects.get_or_create(user=user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], dark_mode=True)
            else:
                UserProfile.objects.get_or_create(user=user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], dark_mode=False)
            return redirect('home')

    return render(request, 'project/addprofile.html', {'user': user, 'form':form})


@login_required(login_url='login')
def editProfile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == "POST":
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        if 'dark_mode' in request.POST:
            profile.dark_mode = True
        else:
            profile.dark_mode = False
        profile.save()
        return redirect('home')

    return render(request, 'project/editprofile.html')