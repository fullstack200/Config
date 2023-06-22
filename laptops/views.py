from django.shortcuts import render
from django.template import loader
from .models import Laptop
from django.http import HttpResponse

# Create your views here.

def progMenu(request):
    myData = Laptop.objects.filter(typ='Programming').values()
    template = loader.get_template('typpro.html')
    context = {
        'prog': myData,
    }
    return HttpResponse(template.render(context, request))

def busnMenu(request):
    myData = Laptop.objects.filter(typ='Business')
    template = loader.get_template('typbus.html')
    context = {
        'busn': myData,
    }
    return HttpResponse(template.render(context, request))

def gameMenu(request):
    myData = Laptop.objects.filter(typ='Gaming')
    template = loader.get_template('typgame.html')
    context = {
        'game': myData,
    }
    return HttpResponse(template.render(context, request))

def gphMenu(request):
    myData = Laptop.objects.filter(typ='Designing')
    template = loader.get_template('typgph.html')
    context = {
        'gph': myData,
    }
    return HttpResponse(template.render(context, request))

def studMenu(request):
    myData = Laptop.objects.filter(typ='Student')
    template = loader.get_template('typstud.html')
    context = {
        'stud': myData,
    }
    return HttpResponse(template.render(context, request))

def typProgramming(request,id):
    myData = Laptop.objects.filter(typ='Programming')
    laptop = Laptop.objects.get(id=id)
    favlaptop = Laptop.objects.filter(user_favourite=request.user, id=laptop.id)
    template = loader.get_template('progView.html')
    context = {
        'prog': myData,
        'laptop':laptop,
        'favlaptop':favlaptop,
    }
    return HttpResponse(template.render(context, request))


def typBusiness(request,id):
    myData = Laptop.objects.filter(typ='Business')
    laptop = Laptop.objects.get(id=id)
    favlaptop = Laptop.objects.filter(user_favourite=request.user,id=laptop.id)
    template = loader.get_template('busnView.html')
    context = {
        'busn': myData,
        'laptop':laptop,
        'favlaptop':favlaptop,
    }
    return HttpResponse(template.render(context, request))

def typGaming(request,id):
    myData = Laptop.objects.filter(typ='Gaming')
    laptop = Laptop.objects.get(id=id)
    favlaptop = Laptop.objects.filter(user_favourite=request.user, id=laptop.id)
    template = loader.get_template('gameView.html')
    context = {
        'game': myData,
        'laptop':laptop,
        'favlaptop':favlaptop,
    }
    return HttpResponse(template.render(context, request))

def typDesigning(request,id):
    myData = Laptop.objects.filter(typ='Designing')
    laptop = Laptop.objects.get(id=id)
    favlaptop = Laptop.objects.filter(user_favourite=request.user, id=laptop.id)
    template = loader.get_template('gphView.html')
    context = {
        'gph': myData,
        'laptop':laptop,
        'favlaptop':favlaptop,
    }
    return HttpResponse(template.render(context, request))

def typStudent(request,id):
    myData = Laptop.objects.filter(typ='Student')
    laptop = Laptop.objects.get(id=id)
    favlaptop = Laptop.objects.filter(user_favourite=request.user, id=laptop.id)
    template = loader.get_template('studView.html')
    context = {
        'stud': myData,
        'laptop':laptop,
        'favlaptop':favlaptop,
    }
    return HttpResponse(template.render(context, request))



