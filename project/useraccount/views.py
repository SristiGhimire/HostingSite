from django.shortcuts import render, redirect
# from account.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .decorators import login_required

# Create your views here.
def signin(request):
    return render(request, 'useraccount/sign-in.html')

def login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        if request.method == "POST":
            email = request.POST['useremail']
            password = request.POST['password']
            user_obj = authenticate(email=email, password=password)
            if not user_obj:
                messages.warning(request, "Invalid username and password...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # Check the user's role and redirect accordingly
            if user_obj.is_admin:
                auth.login(request, user_obj)
                messages.success(request, "Admin login successful!")
                return redirect('dashboard:index')
            # elif user_obj.is_user:
            #     auth.login(request, user_obj)
            #     messages.success(request, "User login successful!")
            #     return redirect('dashboard:index')
            
            else:
                messages.warning(request, 'Invalid Password')
            return redirect('dashboard:index')
        return render(request, 'useraccount/sign-in.html')
    except Exception as e:
        messages.warning(request, 'Something went wrong...')
        return render(request, 'useraccount/sign-in.html')
        

# @login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('useraccount:login')



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('useraccount:login')
        else:
            messages.error(request,form.errors) 
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'useraccount/change_password.html', {'form': form})