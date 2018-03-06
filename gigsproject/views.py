from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world! You're at the Gigs index.")

def about(request):
    return HttpResponse("This is the about page. Created by lab group 4 team d.")
