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
    context = {
        'laptop':laptop,
    }
    return HttpResponse(template.render(context, request))

def is_valid_queryparam(param):
    return param != '' and param is not None

def filterProg(request):
    laptops = Laptop.objects.filter(typ='Programming')
    var = 0
    
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

    filteredList= []
    if request.GET:
        var = 1
        if is_valid_queryparam(brand1):
            a = laptops.filter(brand__icontains=brand1)   
            if a not in filteredList:
                filteredList += a
            else:
                pass
            
        if is_valid_queryparam(brand2):
            b = laptops.filter(brand__icontains=brand2)   
            filteredList += b
            
        if is_valid_queryparam(brand3):
            c = laptops.filter(brand__icontains=brand3)
            filteredList += c
            
        if is_valid_queryparam(brand4):
            d = laptops.filter(brand__icontains=brand4)   
            filteredList += d

        if is_valid_queryparam(brand5):
            e = laptops.filter(brand__icontains=brand5)   
            filteredList += e
        
        if is_valid_queryparam(brand6):
            f = laptops.filter(brand__icontains=brand6)   
            filteredList += f
        
        if is_valid_queryparam(price1):
            g = laptops.filter(price__gt=40000) and laptops.filter(price__lt=50000)
            filteredList += g
            
        if is_valid_queryparam(price2):
            h = laptops.filter(price__gt=50000) and laptops.filter(price__lt=60000)
            filteredList += h

        if is_valid_queryparam(price3):
            i = laptops.filter(price__gt=60000) and laptops.filter(price__lt=70000)
            filteredList += i

        if is_valid_queryparam(price4):
            j = laptops.filter(price__gt=70000) and laptops.filter(price__lt=80000)
            filteredList += j

        if is_valid_queryparam(price5):
            k = laptops.filter(price__gt=80000) and laptops.filter(price__lt=90000)
            filteredList += k

        if is_valid_queryparam(price6):
            l = laptops.filter(price__gt=90000) 
            filteredList += l

    if filteredList != []:  
        laptops = filteredList
    
    elif filteredList == [] and var == 1:
        context = {
            'nofilter':filteredList
        }
        return render(request,'typprolist.html',context)
    
    context = {
    'prog':laptops,
    }
    return render(request,'typprolist.html',context)

