from django.urls import path
from .views import *

urlpatterns = [
    path('category/typpro/view/<int:id>',typProgramming,name='progView'),
    path('category/typbus/view/<int:id>',typBusiness,name='busnView'),
    path('category/typgame/view/<int:id>',typGaming,name='gameView'),
    path('category/typgph/view/<int:id>',typDesigning,name='gphView'),
    path('category/typstud/view/<int:id>',typStudent,name='studView'),
]