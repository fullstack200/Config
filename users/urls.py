from django.urls import path
from laptops.views import *
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/typpro/', progMenu, name='typpro'),
    path('category/typbus/', busnMenu, name='typbus'),
    path('category/typgame/', gameMenu, name='typgame'),
    path('category/typgph/', gphMenu, name='typgph'),
    path('category/typstud/', studMenu, name='typstud'),
    # wishlist URL
    path('favourites',favouritesView,name='favouritesView'),
    path('favourites_add/<int:id>',user_favourite, name="favourites"),
    path('search_result',search.as_view(),name="search_result"),
]
