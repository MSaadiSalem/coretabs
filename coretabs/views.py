from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi there, this is our new home page.")


def hello(request, name):
    return HttpResponse("Hello {}".format(name))
