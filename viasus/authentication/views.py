from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class View_Register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register.html", {"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect("catalogue")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "register.html", {"form":form})
        
def close_session(request):
    logout(request)
    return redirect("catalogue")

def user_login(request):
    if (request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "credenciales invalidas")
                return render(request, "login.html", {'form':form})
        else:
            messages.error(request, "credenciales invalidas")
            return render(request, "login.html", {'form':form})

    form = AuthenticationForm
    return render(request, "login.html", {'form':form})