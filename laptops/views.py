from turtle import update
from django.shortcuts import render
from django.template import loader
from .models import Laptop
from django.db.models import Q
from django.http import HttpResponse

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

    favlaptop = Laptop.objects.filter(
        user_favourite=request.user, id=laptop.id)
    context = {
        'laptop': laptop,
        'favlaptop': favlaptop,
    }
    return HttpResponse(template.render(context, request))


def is_valid_queryparam(param):
    return param != '' and param is not None


def filterProg(request):
    laptops = Laptop.objects.filter(typ='Programming')
   
    if request.GET:     
    # Brands
        brand1 = request.GET.get('apple')
        brand2 = request.GET.get('hp')
        brand3 = request.GET.get('dell')
        brand4 = request.GET.get('asus')
        brand5 = request.GET.get('lg')
        brand6 = request.GET.get('samsung')
        brand7 = request.GET.get('razer-blade')

        # Price
        price = request.GET.get('price')

        # Processor
        processor1 = request.GET.get('processor1')
        processor2 = request.GET.get('processor2')
        processor3 = request.GET.get('processor3')
    
        # RAM
        ram1 = request.GET.get('ram1')
        ram2 = request.GET.get('ram2')
        ram3 = request.GET.get('ram3')
        ram4 = request.GET.get('ram4')
        ram5 = request.GET.get('ram5')

        # Storage
        storage1 = request.GET.get('storage1')
        storage2 = request.GET.get('storage2')
        storage3 = request.GET.get('storage3')
        storage4 = request.GET.get('storage4')

        # Graphics
        graphics1 = request.GET.get('graphics1')
        graphics2 = request.GET.get('graphics2')
        graphics3 = request.GET.get('graphics3')

        dictionary = {'brand__in':[brand1,brand2,brand3,brand4,brand5,brand6,brand7],'price__range':price,'processorBrand__in':[processor1,processor2,processor3],'ram__in':[ram1,ram2,ram3,ram4,ram5],'storageMemory__in':[storage1,storage2,storage3,storage4],'graphicsMemory__in':[graphics1,graphics2,graphics3]}
        if dictionary['price__range'] is not None:
            if int(dictionary['price__range']) > 90000:
                dictionary.pop('price__range')
                dictionary.update({'price__gt':90000})
            else:
                dictionary['price__range'] = (int(price)-10000, price)

        for i, j in dictionary.items():
            if i == 'price__range' or i == 'price__gt':
                continue
            else:
                while None in j:
                    j.remove(None)
        
        updated_dictionary = {k:v for k, v in dictionary.items() if v}

        for key,value in updated_dictionary.items():
            if key == 'price__range' or i == 'price__gt':
                continue
            else:
                for i in value:
                    if type(i) == str:
                        continue
                    elif i.isdigit():
                        intVal = int(i)
                        value.remove(i)
                        value.append(intVal)

        filterList = Laptop.objects.filter(typ='Programming',**updated_dictionary)

        if not filterList:
            filterList = 0

        context = {
            'filter': filterList,
            }
        return render(request,'typprolist.html',context)
        
        
    context = {
        'prog':laptops,
    }
    return render(request,'typprolist.html',context)

def filterBusn(request):
    laptops = Laptop.objects.filter(typ='Business')
   
    if request.GET:     
    # Brands
        brand1 = request.GET.get('apple')
        brand2 = request.GET.get('hp')
        brand3 = request.GET.get('dell')
        brand4 = request.GET.get('asus')
        brand5 = request.GET.get('lg')
        brand6 = request.GET.get('samsung')
        brand7 = request.GET.get('razer-blade')

        # Price
        price = request.GET.get('price')

        # Processor
        processor1 = request.GET.get('processor1')
        processor2 = request.GET.get('processor2')
        processor3 = request.GET.get('processor3')
    
        # RAM
        ram1 = request.GET.get('ram1')
        ram2 = request.GET.get('ram2')
        ram3 = request.GET.get('ram3')
        ram4 = request.GET.get('ram4')
        ram5 = request.GET.get('ram5')

        # Storage
        storage1 = request.GET.get('storage1')
        storage2 = request.GET.get('storage2')
        storage3 = request.GET.get('storage3')
        storage4 = request.GET.get('storage4')

        # Graphics
        graphics1 = request.GET.get('graphics1')
        graphics2 = request.GET.get('graphics2')
        graphics3 = request.GET.get('graphics3')

        dictionary = {'brand__in':[brand1,brand2,brand3,brand4,brand5,brand6,brand7],'price__range':price,'processorBrand__in':[processor1,processor2,processor3],'ram__in':[ram1,ram2,ram3,ram4,ram5],'storageMemory__in':[storage1,storage2,storage3,storage4],'graphicsMemory__in':[graphics1,graphics2,graphics3]}
        if dictionary['price__range'] is not None:
            if int(dictionary['price__range']) > 90000:
                dictionary.pop('price__range')
                dictionary.update({'price__gt':90000})
            else:
                dictionary['price__range'] = (int(price)-10000, price)

        for i, j in dictionary.items():
            if i == 'price__range' or i == 'price__gt':
                continue
            else:
                while None in j:
                    j.remove(None)
        
        updated_dictionary = {k:v for k, v in dictionary.items() if v}

        for key,value in updated_dictionary.items():
            if key == 'price__range' or i == 'price__gt':
                continue
            else:
                for i in value:
                    if type(i) == str:
                        continue
                    elif i.isdigit():
                        intVal = int(i)
                        value.remove(i)
                        value.append(intVal)

        filterList = Laptop.objects.filter(**updated_dictionary)

        if not filterList:
            filterList = 0

        context = {
            'filter': filterList,
            }
        return render(request,'typbuslist.html',context)
        
        
    context = {
        'busn':laptops,
    }
    return render(request,'typbuslist.html',context)

def filterGame(request):
    laptops = Laptop.objects.filter(typ='Gaming')
   
    if request.GET:     
    # Brands
        brand1 = request.GET.get('apple')
        brand2 = request.GET.get('hp')
        brand3 = request.GET.get('dell')
        brand4 = request.GET.get('asus')
        brand5 = request.GET.get('lg')
        brand6 = request.GET.get('samsung')
        brand7 = request.GET.get('razer-blade')

        # Price
        price = request.GET.get('price')

        # Processor
        processor1 = request.GET.get('processor1')
        processor2 = request.GET.get('processor2')
        processor3 = request.GET.get('processor3')
    
        # RAM
        ram1 = request.GET.get('ram1')
        ram2 = request.GET.get('ram2')
        ram3 = request.GET.get('ram3')
        ram4 = request.GET.get('ram4')
        ram5 = request.GET.get('ram5')

        # Storage
        storage1 = request.GET.get('storage1')
        storage2 = request.GET.get('storage2')
        storage3 = request.GET.get('storage3')
        storage4 = request.GET.get('storage4')

        # Graphics
        graphics1 = request.GET.get('graphics1')
        graphics2 = request.GET.get('graphics2')
        graphics3 = request.GET.get('graphics3')

        dictionary = {'brand__in':[brand1,brand2,brand3,brand4,brand5,brand6,brand7],'price__range':price,'processorBrand__in':[processor1,processor2,processor3],'ram__in':[ram1,ram2,ram3,ram4,ram5],'storageMemory__in':[storage1,storage2,storage3,storage4],'graphicsMemory__in':[graphics1,graphics2,graphics3]}
        if dictionary['price__range'] is not None:
            if int(dictionary['price__range']) > 90000:
                dictionary.pop('price__range')
                dictionary.update({'price__gt':90000})
            else:
                dictionary['price__range'] = (int(price)-10000, price)

        for i, j in dictionary.items():
            if i == 'price__range' or i == 'price__gt':
                continue
            else:
                while None in j:
                    j.remove(None)
        
        updated_dictionary = {k:v for k, v in dictionary.items() if v}

        for key,value in updated_dictionary.items():
            if key == 'price__range' or i == 'price__gt':
                continue
            else:
                for i in value:
                    if type(i) == str:
                        continue
                    elif i.isdigit():
                        intVal = int(i)
                        value.remove(i)
                        value.append(intVal)

        filterList = Laptop.objects.filter(**updated_dictionary)

        if not filterList:
            filterList = 0

        context = {
            'filter': filterList,
            }
        return render(request,'typgamelist.html',context)
        
        
    context = {
        'game':laptops,
    }
    return render(request,'typgamelist.html',context)

def filterGraphics(request):
    laptops = Laptop.objects.filter(typ='Designing')
   
    if request.GET:     
    # Brands
        brand1 = request.GET.get('apple')
        brand2 = request.GET.get('hp')
        brand3 = request.GET.get('dell')
        brand4 = request.GET.get('asus')
        brand5 = request.GET.get('lg')
        brand6 = request.GET.get('samsung')
        brand7 = request.GET.get('razer-blade')

        # Price
        price = request.GET.get('price')

        # Processor
        processor1 = request.GET.get('processor1')
        processor2 = request.GET.get('processor2')
        processor3 = request.GET.get('processor3')
    
        # RAM
        ram1 = request.GET.get('ram1')
        ram2 = request.GET.get('ram2')
        ram3 = request.GET.get('ram3')
        ram4 = request.GET.get('ram4')
        ram5 = request.GET.get('ram5')

        # Storage
        storage1 = request.GET.get('storage1')
        storage2 = request.GET.get('storage2')
        storage3 = request.GET.get('storage3')
        storage4 = request.GET.get('storage4')

        # Graphics
        graphics1 = request.GET.get('graphics1')
        graphics2 = request.GET.get('graphics2')
        graphics3 = request.GET.get('graphics3')

        dictionary = {'brand__in':[brand1,brand2,brand3,brand4,brand5,brand6,brand7],'price__range':price,'processorBrand__in':[processor1,processor2,processor3],'ram__in':[ram1,ram2,ram3,ram4,ram5],'storageMemory__in':[storage1,storage2,storage3,storage4],'graphicsMemory__in':[graphics1,graphics2,graphics3]}
        if dictionary['price__range'] is not None:
            if int(dictionary['price__range']) > 90000:
                dictionary.pop('price__range')
                dictionary.update({'price__gt':90000})
            else:
                dictionary['price__range'] = (int(price)-10000, price)

        for i, j in dictionary.items():
            if i == 'price__range' or i == 'price__gt':
                continue
            else:
                while None in j:
                    j.remove(None)
        
        updated_dictionary = {k:v for k, v in dictionary.items() if v}

        for key,value in updated_dictionary.items():
            if key == 'price__range' or i == 'price__gt':
                continue
            else:
                for i in value:
                    if type(i) == str:
                        continue
                    elif i.isdigit():
                        intVal = int(i)
                        value.remove(i)
                        value.append(intVal)

        filterList = Laptop.objects.filter(**updated_dictionary)

        if not filterList:
            filterList = 0

        context = {
            'filter': filterList,
            }
        return render(request,'typdesglist.html',context)
        
        
    context = {
        'desg':laptops,
    }
    return render(request,'typdesglist.html',context)

def filterStudent(request):
    laptops = Laptop.objects.filter(typ='Student')
   
    if request.GET:     
    # Brands
        brand1 = request.GET.get('apple')
        brand2 = request.GET.get('hp')
        brand3 = request.GET.get('dell')
        brand4 = request.GET.get('asus')
        brand5 = request.GET.get('lg')
        brand6 = request.GET.get('samsung')
        brand7 = request.GET.get('razer-blade')

        # Price
        price = request.GET.get('price')

        # Processor
        processor1 = request.GET.get('processor1')
        processor2 = request.GET.get('processor2')
        processor3 = request.GET.get('processor3')
    
        # RAM
        ram1 = request.GET.get('ram1')
        ram2 = request.GET.get('ram2')
        ram3 = request.GET.get('ram3')
        ram4 = request.GET.get('ram4')
        ram5 = request.GET.get('ram5')

        # Storage
        storage1 = request.GET.get('storage1')
        storage2 = request.GET.get('storage2')
        storage3 = request.GET.get('storage3')
        storage4 = request.GET.get('storage4')

        # Graphics
        graphics1 = request.GET.get('graphics1')
        graphics2 = request.GET.get('graphics2')
        graphics3 = request.GET.get('graphics3')

        dictionary = {'brand__in':[brand1,brand2,brand3,brand4,brand5,brand6,brand7],'price__range':price,'processorBrand__in':[processor1,processor2,processor3],'ram__in':[ram1,ram2,ram3,ram4,ram5],'storageMemory__in':[storage1,storage2,storage3,storage4],'graphicsMemory__in':[graphics1,graphics2,graphics3]}
        if dictionary['price__range'] is not None:
            if int(dictionary['price__range']) > 90000:
                dictionary.pop('price__range')
                dictionary.update({'price__gt':90000})
            else:
                dictionary['price__range'] = (int(price)-10000, price)

        for i, j in dictionary.items():
            if i == 'price__range' or i == 'price__gt':
                continue
            else:
                while None in j:
                    j.remove(None)
        
        updated_dictionary = {k:v for k, v in dictionary.items() if v}

        for key,value in updated_dictionary.items():
            if key == 'price__range' or i == 'price__gt':
                continue
            else:
                for i in value:
                    if type(i) == str:
                        continue
                    elif i.isdigit():
                        intVal = int(i)
                        value.remove(i)
                        value.append(intVal)

        filterList = Laptop.objects.filter(**updated_dictionary)

        if not filterList:
            filterList = 0

        context = {
            'filter': filterList,
            }
        return render(request,'typstudlist.html',context)
        
        
    context = {
        'stud':laptops,
    }
    return render(request,'typstudlist.html',context)