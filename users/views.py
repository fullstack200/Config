from multiprocessing import context
from re import L
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from laptops.models import Laptop
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home_page.html'
   
class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class CategoryView(LoginRequiredMixin,TemplateView):
    template_name = 'main1.html'
    login_url = 'login'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"

def favouritesView(request):
    laptops = Laptop.objects.filter(user_favourite=request.user)
    return render(request, 'fav.html', {"list":laptops})

def user_favourite(request, id):
    laptop = get_object_or_404(Laptop,id=id)
    if laptop.user_favourite.filter(id=request.user.id).exists():
        laptop.user_favourite.remove(request.user)
    else:
        laptop.user_favourite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class search(ListView):
    model = Laptop
    context_object_name = 'queryset'
    template_name = "searchView.html"
    
    def get_queryset(self):
        query = self.request.GET.get('searchlaptop')
        return Laptop.objects.filter(
            Q(model__icontains = query) | Q(brand__icontains = query)
            )

