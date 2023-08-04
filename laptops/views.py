from genericpath import exists
from re import L
from django.shortcuts import render
from django.template import loader
from .models import Laptop
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView
from itertools import chain

# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None

def progDesc(request):
    myData = Laptop.objects.filter(typ='Programming')
    template = loader.get_template('typpro.html')
    context = {
        'prog': myData,
    }
    return HttpResponse(template.render(context, request))

def busnDesc(request):
    myData = Laptop.objects.filter(typ='Business')
    template = loader.get_template('typbus.html')
    context = {
        'busn': myData,
    }
    return HttpResponse(template.render(context, request))

def gameDesc(request):
    myData = Laptop.objects.filter(typ='Gaming')
    template = loader.get_template('typgame.html')
    context = {
        'game': myData,
    }
    return HttpResponse(template.render(context, request))

def gphDesc(request):
    myData = Laptop.objects.filter(typ='Designing')
    template = loader.get_template('typgph.html')
    context = {
        'gph': myData,
    }
    return HttpResponse(template.render(context, request))

def studDesc(request):
    myData = Laptop.objects.filter(typ='Student')
    template = loader.get_template('typstud.html')
    context = {
        'stud': myData,
    }
    return HttpResponse(template.render(context, request))

            
def laptopView(request, id):
    laptop = Laptop.objects.get(id=id)
    if laptop.typ == "Programming":
        template = loader.get_template('progView.html')
    if laptop.typ == "Business":
        template = loader.get_template('busnView.html')
    if laptop.typ == "Gaming":
        template = loader.get_template('gameView.html')
    if laptop.typ == "Designing":
        template = loader.get_template('gphView.html')
    if laptop.typ == "Student":
        template = loader.get_template('studView.html')
    
    favlaptop = Laptop.objects.filter(user_favourite=request.user, id=laptop.id)
    context = {
        'laptop':laptop,
        'favlaptop':favlaptop,
    }
    return HttpResponse(template.render(context, request))

def is_valid_queryparam(param):
    return param != '' and param is not None

def filterProg(request):
    laptops = Laptop.objects.filter(typ='Programming')
        
    #Brands
    brand1 = request.GET.get('apple')
    brand2 = request.GET.get('hp')
    brand3 = request.GET.get('dell')
    brand4 = request.GET.get('asus')
    brand5 = request.GET.get('lg')
    brand6 = request.GET.get('samsung')

    #Price
    price1 = request.GET.get('price1')
    price2 = request.GET.get('price2')
    price3 = request.GET.get('price3')
    price4 = request.GET.get('price4')
    price5 = request.GET.get('price5')
    price6 = request.GET.get('price6')

    #Processor
    processor1 = request.GET.get('processor1')
    processor2 = request.GET.get('processor2')
    processor3 = request.GET.get('processor3')
    processor4 = request.GET.get('processor4')

    #RAM
    ram1 = request.GET.get('ram1')
    ram2 = request.GET.get('ram2')
    ram3 = request.GET.get('ram3')
    ram4 = request.GET.get('ram4')
    ram5 = request.GET.get('ram5')

    #Storage
    storage1 = request.GET.get('storage1')
    storage2 = request.GET.get('storage2')
    storage3 = request.GET.get('storage3')
    storage4 = request.GET.get('storage4')

    #Graphics
    graphics1 = request.GET.get('graphics1')
    graphics2 = request.GET.get('graphics2')
    graphics3 = request.GET.get('graphics3')

    context = {
    'prog':laptops,
    }
    return render(request,'typprolist.html',context)