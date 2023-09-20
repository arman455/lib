from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "Main/index.html") 

def book(request):
    return render(request, "Book/index.html")

def auther(request):
    return render(request, "Auther/index.html")
