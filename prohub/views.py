from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')


def profile(request):
    return render(request,'profile.html')