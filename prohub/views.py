from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,ReviewRating
from django.shortcuts import get_object_or_404
from .forms import ReviewForm




# Create your views here.
def home(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']

        new_project = Project(owner=request.user,image=image,title=title,description=description,location=location)
        new_project.save()
    projects = Project.objects.all()
    profile = Profile.objects.all()
    return render(request,'index.html',{'projects':projects,'profile':profile})

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
    user = request.user.id
    project = Project.objects.filter(owner_id=user)
    print('###')
    print(project)
    if request.method == 'POST':
        profile_picture = request.FILES.get('image')
        name = request.POST['name']
        bio = request.POST['bio']

        profile = Profile(profile_picture=profile_picture,name=name,bio=bio,user=request.user)
        profile.save()
        return render(request,'profile.html',{'profile':profile,'project':project})
    return render(request,'profile.html',{'project':project})

# details view
@login_required
def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    profile = Profile.objects.all()
    reviews = ReviewRating.objects.filter(project_id=id)
    return render(request,'project-detail.html',{'project':project,'profile':profile,'reviews':reviews})


# Reviews function
def submit_review(request,project_id):
    users = request.user
    if request.method == 'POST':
        subject = request.POST['subject']
        review = request.POST['review']
        rating = request.POST['rating']

        user = request.user.id
        get_reviews = ReviewRating.objects.filter(project_id=project_id,user_id=user).exists()
        if get_reviews:
            get_reviews = ReviewRating.objects.get(project_id=project_id,user_id=user)
            get_reviews.rating = rating
            get_reviews.subject = subject
            get_reviews.review = review
            get_reviews.save()
        else:
            project = Project.objects.get(id=project_id)
            reviews = ReviewRating(project=project,user=users,subject=subject,review=review,rating=rating)
            reviews.save()
    return redirect('/')


# API SECTION


