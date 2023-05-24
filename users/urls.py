from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/typpro/', ProgrammerView.as_view(), name='typpro'),
    path('category/typbus/', BusinessView.as_view(), name='typbus'),
    path('category/typgame/', GamerView.as_view(), name='typgame'),
    path('category/typgph/', DesignerView.as_view(), name='typgph'),
    path('category/typstud/', StudentView.as_view(), name='typstud'),
]

