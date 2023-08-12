from django.urls import path
from .views import *

urlpatterns = [
    path('category/typpro/list/',filterProg, name='progView'),
    path('category/typbus/list/',filterBusn,name='busnView'),
    path('category/typgame/list/',filterGame,name='gameView'),
    path('category/typgph/list/',filterGraphics,name='gphView'),
    path('category/typstud/list/',filterStudent,name='studView'),
    path('view/<int:id>',laptopView,name='laptopView'),
]

