from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username',)
        password = request.POST.get('password',)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('shop:allProCat')
        else:
            messages.info(request,"invalid credential")
            return redirect("credential:login")
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username',)
        first_name = request.POST.get('first_name',)
        last_name = request.POST.get('last_name',)
        email = request.POST.get('email',)
        password = request.POST.get('password',)
        cpassword = request.POST.get('password1',)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request,"username taken")
                return redirect("credential:register")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"email taken")
                return redirect("credential:register")
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
            return redirect("credential:login")
                
        else:
            messages.info(request,"password missmatched")
            return redirect("credential:register")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('shop:allProCat')