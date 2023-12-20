from django.shortcuts import render
from django.http import HttpResponse



def hello_world(requests):
    print("req")
    print(requests)
    return HttpResponse("<h1>hello world</h1>")
def nav_bar(requests):
    return render(requests,"home\home.html")
def logiin(requests): 
    return render(requests,"home\logiin.html")

# Create your views here.
