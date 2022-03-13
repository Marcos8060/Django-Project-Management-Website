from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from django.shortcuts import get_object_or_404



# Create your views here.
def home(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']

        new_project = Project(user=request.user,image=image,title=title,description=description,location=location)
        new_project.save()
    projects = Project.objects.all()
    return render(request,'index.html',{'projects':projects})

# signUp view
def register(request):    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.save()
            print('user created')
            return redirect('login')
    return render(request,'register.html')

# login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

# logout view
def logout_view(request):
    logout(request)
    return redirect('home')

# profile view
@login_required
def profile(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('image')
        name = request.POST['name']
        bio = request.POST['bio']
        location = request.POST['location']

        profile = Profile(profile_picture=profile_picture,name=name,bio=bio,location=location,user=request.user,project=request.user)
        profile.save()
        projects = Project.objects.filter(project=profile.project)
        return render(request,'profile.html',{'profile':profile,'projects':projects})
    return render(request,'profile.html')

# details view
def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    return render(request,'project-detail.html',{'project':project})