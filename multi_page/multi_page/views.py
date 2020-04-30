from django.shortcuts import render
from . import machinelearning

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = machinelearning.multiplier(user_input)
    return render(request, "result.html", {'home_input': user_input})