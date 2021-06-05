from django.shortcuts import render,HttpResponse

def index(request):
    return render( request, 'index.html')

def team(request):
    return render( request, 'team.html')