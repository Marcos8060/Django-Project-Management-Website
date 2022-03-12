from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html')


def register(request):
    return render(request,'register.html')


def profile(request):
    return render(request,'profile.html')