from django.shortcuts import render

def index(request):
    return render(request,'validation_of_road/index.html')