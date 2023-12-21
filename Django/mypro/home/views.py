from django.shortcuts import render
from django.http import HttpResponse



def hello_world(requests):
    print("req")
    print(requests)
    return HttpResponse("<h1>hello world</h1>")
def nav_bar(requests):
    return render(requests,"home\home.html",{"links":links})
def logiin(requests): 
    return render(requests,"home\logiin.html")
links = ["www.google.com","www.amazon.com","www.youtube.com"]
names = ["Google" ,"Amazon",  "Youtube"]
nam = {"google": "www.google.com",
       "amazon": "www.google.com",
       "youtube": "www.google.com"
       }
# Create your views here.
