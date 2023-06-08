from django.urls import path
from .views import *

urlpatterns = [
    path('typProgramming/view/<int:id>',typProgramming,name='progView'),
    path('typBusiness/view/<int:id>',typBusiness,name='busnView'),
    path('typGaming/view/<int:id>',typGaming,name='gameView'),
    path('typDesigning/view/<int:id>',typDesigning,name='gphView'),
    path('typStudent/view/<int:id>',typStudent,name='studView'),
]