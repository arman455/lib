from django.shortcuts import render

# Create your views here.

def auther(request):
    return render(request, "Auther/index.html")
