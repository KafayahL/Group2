from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import CustomerCreationForm



class SignUpView(generic.CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def home(request):
 return render(request, 'shop/product/list.html',{'shop': home})
