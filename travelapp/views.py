from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def IndexView(request):
    return render(request,'index.html')

