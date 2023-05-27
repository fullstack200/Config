from django.views.generic import TemplateView
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProgrammerView(TemplateView):
    template_name = 'typpro.html'

class BusinessView(TemplateView):
    template_name = 'typbus.html'

class GamerView(TemplateView):
    template_name = 'typgame.html'

class DesignerView(TemplateView):
    template_name = 'typgph.html'

class StudentView(TemplateView):
    template_name = 'typstud.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"