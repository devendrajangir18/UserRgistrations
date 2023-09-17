from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
# password for test user mohit= moh@123***

def index(request):
    # ye django mai anonymous user(jo login nhi h phle se) unko rokne k liye hai 
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
        
    return render(request, 'login.html')
    

def logoutUser(request):
    logout(request)
    return redirect("/login")

# indentation error ko remove krne k liye  syntaxt thikkrna hoga if else wale mai tab deke 