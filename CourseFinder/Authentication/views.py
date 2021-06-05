from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.
def logIn(request):
    if request.method == 'GET':
        return render( request, 'logIn.html' )
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login( request , user )
            return redirect('/search')
        else:
            messages.info( request , 'Invalid Credentials' )
            return redirect('/search')
        return HttpResponse("<h1><center>Successfull</center></h1>")


def signUp(request):
     if request.method == 'GET':
        return render( request, 'signUp.html' )
     else:

        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken' ) 
            return redirect('/logIn/signUp')
        elif User.objects.filter(email=email).exists():   
            messages.info(request, 'Email already Taken' ) 
            return redirect('/logIn/signUp')
        else:
            user = User.objects.create_user( username=username , password = password , email = email , first_name = name )
            user.save()
            auth.login( request , user )
            return redirect( '/search' )
         
        
