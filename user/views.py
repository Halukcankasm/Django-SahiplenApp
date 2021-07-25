from django.shortcuts import render,redirect
from .forms import RegisterForm , LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def register(requset):

    form = RegisterForm(requset.POST or None)

    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
            
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(requset,newUser)
        messages.success(requset,"Başarıyla kayıt oldunuz...")
        return redirect("index")

    context = {"form" : form}
    return render(requset,"register.html",context)

def loginUser(requset):
    form = LoginForm(requset.POST or None)

    context = { "form":form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username , password = password)

        if user is None:
            messages.info(requset,"kullanıcı Adı veya Parola Hatalı")
            return render(requset,"login.html",context)
        messages.success(requset,"Başarıyla Giriş Yaptınız...")
        login(requset,user)
        return redirect("index")
    return render(requset,"login.html",context)

def logoutUser(requset):
    logout(requset)
    messages.success(requset,"Başarıyla Çıkış Yaptınız")
    return redirect("index")