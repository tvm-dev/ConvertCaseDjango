from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>I'm Home!</h1>")

def convertCase(request):
    return render(request, 'pages/convertCase.html')

def tests(request):
    return render(request, 'pages/tests.html')

def privacy(request):
    return render(request, 'pages/privacy-policy.html')

    
def terms(request):
    return render(request, 'pages/terms.html')





